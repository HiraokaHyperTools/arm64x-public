ARM64 プロセスから LocalDB を操作
=======================================================

概要
----

ARM64 プロセスから `SQL Server Express LocalDB インスタンス API <https://learn.microsoft.com/ja-jp/sql/relational-databases/express-localdb-instance-apis/sql-server-express-localdb-reference-instance-apis?view=sql-server-ver17>`_ を使用して LocalDB を操作しようとする一切の操作が失敗します

身近な所では .NET Framework または .NET に標準装備の System.Data.SqlClient による LocalDB 起動操作の失敗が挙げられます

例えば SqlConnection Class を用いて ``server=(localdb)\myInstance`` へ接続しようとするときです

このとき SqlConnection の内部では ``LocalDBCreateInstance`` API を使用して LocalDB を起動しようとします

これは、プロセスに対して ``SqlUserInstance.dll`` を読み込もうとします

``SqlUserInstance.dll`` インストール先の例:

.. code-block:: text

   C:\Program Files\Microsoft SQL Server\110\LocalDB\Binn\SqlUserInstance.dll
   C:\Program Files\Microsoft SQL Server\120\LocalDB\Binn\SqlUserInstance.dll
   C:\Program Files\Microsoft SQL Server\130\LocalDB\Binn\SqlUserInstance.dll
   C:\Program Files\Microsoft SQL Server\150\LocalDB\Binn\SqlUserInstance.dll

しかし ``SqlUserInstance.dll`` は x86 or x64 版しか提供されていないため、 ARM64 プロセスへの読み込みは失敗します

.. code:: text

   Unhandled exception. Microsoft.Data.SqlClient.SqlException (0x80131904): A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: SQL Network Interfaces, error: 56 - Unable to load the SQLUserInstance.dll from the location specified in the registry. Verify that the Local Database Runtime feature of SQL Server Express is properly installed.)
    ---> System.ComponentModel.Win32Exception (193): %1 は有効な Win32 アプリケーションではありません。
      at Microsoft.Data.SqlClient.SqlInternalConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)
      at Microsoft.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(TdsParserStateObject stateObj, Boolean callerHasConnectionLock, Boolean asyncClose)
      at Microsoft.Data.SqlClient.TdsParser.Connect(ServerInfo serverInfo, SqlInternalConnectionTds connHandler, Boolean ignoreSniOpenTimeout, Int64 timerExpire, SqlConnectionString connectionOptions, Boolean withFailover)
      at Microsoft.Data.SqlClient.SqlInternalConnectionTds.AttemptOneLogin(ServerInfo serverInfo, String newPassword, SecureString newSecurePassword, Boolean ignoreSniOpenTimeout, TimeoutTimer timeout, Boolean withFailover)
      at Microsoft.Data.SqlClient.SqlInternalConnectionTds.LoginNoFailover(ServerInfo serverInfo, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance, SqlConnectionString connectionOptions, SqlCredential credential, TimeoutTimer timeout)
      at Microsoft.Data.SqlClient.SqlInternalConnectionTds.OpenLoginEnlist(TimeoutTimer timeout, SqlConnectionString connectionOptions, SqlCredential credential, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance)
      at Microsoft.Data.SqlClient.SqlInternalConnectionTds..ctor(DbConnectionPoolIdentity identity, SqlConnectionString connectionOptions, SqlCredential credential, Object providerInfo, String newPassword, SecureString newSecurePassword, Boolean redirectedUserInstance, SqlConnectionString userConnectionOptions, SessionData reconnectSessionData, Boolean applyTransientFaultHandling, String accessToken, DbConnectionPool pool)
      at Microsoft.Data.SqlClient.SqlConnectionFactory.CreateConnection(DbConnectionOptions options, DbConnectionPoolKey poolKey, Object poolGroupProviderInfo, DbConnectionPool pool, DbConnection owningConnection, DbConnectionOptions userOptions)
      at Microsoft.Data.ProviderBase.DbConnectionFactory.CreatePooledConnection(DbConnectionPool pool, DbConnection owningObject, DbConnectionOptions options, DbConnectionPoolKey poolKey, DbConnectionOptions userOptions)
      at Microsoft.Data.ProviderBase.DbConnectionPool.CreateObject(DbConnection owningObject, DbConnectionOptions userOptions, DbConnectionInternal oldConnection)
      at Microsoft.Data.ProviderBase.DbConnectionPool.UserCreateRequest(DbConnection owningObject, DbConnectionOptions userOptions, DbConnectionInternal oldConnection)
      at Microsoft.Data.ProviderBase.DbConnectionPool.TryGetConnection(DbConnection owningObject, UInt32 waitForMultipleObjectsTimeout, Boolean allowCreate, Boolean onlyOneCheckConnection, DbConnectionOptions userOptions, DbConnectionInternal& connection)
      at Microsoft.Data.ProviderBase.DbConnectionPool.TryGetConnection(DbConnection owningObject, TaskCompletionSource`1 retry, DbConnectionOptions userOptions, DbConnectionInternal& connection)
      at Microsoft.Data.ProviderBase.DbConnectionFactory.TryGetConnection(DbConnection owningConnection, TaskCompletionSource`1 retry, DbConnectionOptions userOptions, DbConnectionInternal oldConnection, DbConnectionInternal& connection)
      at Microsoft.Data.ProviderBase.DbConnectionInternal.TryOpenConnectionInternal(DbConnection outerConnection, DbConnectionFactory connectionFactory, TaskCompletionSource`1 retry, DbConnectionOptions userOptions)
      at Microsoft.Data.ProviderBase.DbConnectionClosed.TryOpenConnection(DbConnection outerConnection, DbConnectionFactory connectionFactory, TaskCompletionSource`1 retry, DbConnectionOptions userOptions)
      at Microsoft.Data.SqlClient.SqlConnection.TryOpen(TaskCompletionSource`1 retry, SqlConnectionOverrides overrides)
      at Microsoft.Data.SqlClient.SqlConnection.Open(SqlConnectionOverrides overrides)
      at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerConnection.OpenDbConnection(Boolean errorsExpected)
      at Microsoft.EntityFrameworkCore.Storage.RelationalConnection.OpenInternal(Boolean errorsExpected)
      at Microsoft.EntityFrameworkCore.Storage.RelationalConnection.Open(Boolean errorsExpected)
      at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerDatabaseCreator.<>c__DisplayClass18_0.<Exists>b__0(DateTime giveUp)
      at Microsoft.EntityFrameworkCore.ExecutionStrategyExtensions.<>c__DisplayClass12_0`2.<Execute>b__0(DbContext _, TState s)
      at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerExecutionStrategy.Execute[TState,TResult](TState state, Func`3 operation, Func`3 verifySucceeded)
      at Microsoft.EntityFrameworkCore.ExecutionStrategyExtensions.Execute[TState,TResult](IExecutionStrategy strategy, TState state, Func`2 operation, Func`2 verifySucceeded)
      at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerDatabaseCreator.Exists(Boolean retryOnNotExists)
      at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerDatabaseCreator.Exists()
      at Microsoft.EntityFrameworkCore.Storage.RelationalDatabaseCreator.EnsureCreated()
      at Microsoft.EntityFrameworkCore.Infrastructure.DatabaseFacade.EnsureCreated()
      ...
   ClientConnectionId:00000000-0000-0000-0000-000000000000
   Error Number:193,State:0,Class:20

現状
----

既に多方面で議論されています。 2026-01-19 現在、公式からの解決策は未だ提示されていません:

- `SQL LocalDB broken on ARM64 - Developer Community <https://developercommunity.visualstudio.com/t/SQL-LocalDB-broken-on-ARM64/10107793>`_
- `"Unable to load the SQLUserInstance.dll" when connecting to LocalDB on ARM64 (Win Dev Kit 2023) - Developer Community <https://developercommunity.visualstudio.com/t/Unable-to-load-the-SQLUserInstancedll/10188568>`_
- `SQL Server LocalDB on Windows on ARM - Microsoft Q&A <https://learn.microsoft.com/en-us/answers/questions/1856766/sql-server-localdb-on-windows-on-arm>`_
- `Cannot connect to (localdb) from .NET Core except via Named Pipe on Windows 11 ARM · Issue #1441 · dotnet/SqlClient <https://github.com/dotnet/SqlClient/issues/1441>`_

公式回答
-------------------

`“Unable to load the SQLUserInstance.dll” when connecting to LocalDB on ARM64 (Win Dev Kit 2023) - Developer Community <https://developercommunity.visualstudio.com/t/Unable-to-load-the-SQLUserInstancedll/10188568>`_ (Jul 03, 2024 5:24 AM) によると、問題の把握はしているが、修正の予定は無い、とのこと

.. pull-quote::

   Connectivity to SQLLocalDB on arm64 remains on our roadmap, but we do not have a release that I can commit to at this time. We understand that connecting to LocalDB dramatically simplifies the SQL projects development process. You may find installing SQL Server developer edition on the local arm64 Windows machine for developer purposes to be a suitable workaround.

回避策 (運用面)
-------------------

* Microsoft SQL Server Express (または Developer など) のインスタンスをインストールします。 LocalDB の代わりに、そちらへ接続するようにします
* 対象アプリを x64 プロセスとして実行します

回避策 (設計面)
-------------------

* ``.NET Aspire`` のようなオーケストレーションを採用して `SQL Server integration <https://aspire.dev/integrations/databases/sql-server/>`_ (Docker 技術利用) を活用する案もあります。 しかし、当の `mcr.microsoft.com/mssql/server <https://hub.docker.com/r/microsoft/mssql-server>`_ イメージについても amd64 版しか存在しないようです。 Docker を利用する場合についても x64 版を導入するなど、更なる労力を費やす必要があるようです
