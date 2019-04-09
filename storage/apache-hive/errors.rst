Hive Error
==========

MapredLocalTask
---------------

Error: Error while processing statement: FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.mr.MapredLocalTask (state=08S01,code=1)


.. code-block:: text


    java.io.IOException: Cannot run program "/usr/lib/hadoop/bin/hadoop" (in directory "/root"): error=13, Permission denied
            at java.lang.ProcessBuilder.start(ProcessBuilder.java:1047)
            at java.lang.Runtime.exec(Runtime.java:617)
            at java.lang.Runtime.exec(Runtime.java:450)
            at org.apache.hadoop.hive.ql.exec.mr.MapredLocalTask.executeInChildVM(MapredLocalTask.java:325)
            at org.apache.hadoop.hive.ql.exec.mr.MapredLocalTask.execute(MapredLocalTask.java:156)
            at org.apache.hadoop.hive.ql.exec.Task.executeTask(Task.java:214)
            at org.apache.hadoop.hive.ql.exec.TaskRunner.runSequential(TaskRunner.java:99)
            at org.apache.hadoop.hive.ql.Driver.launchTask(Driver.java:2054)
            at org.apache.hadoop.hive.ql.Driver.execute(Driver.java:1750)
            at org.apache.hadoop.hive.ql.Driver.runInternal(Driver.java:1503)
            at org.apache.hadoop.hive.ql.Driver.run(Driver.java:1287)
            at org.apache.hadoop.hive.ql.Driver.run(Driver.java:1282)
            at org.apache.hive.service.cli.operation.SQLOperation.runQuery(SQLOperation.java:236)
            at org.apache.hive.service.cli.operation.SQLOperation.runInternal(SQLOperation.java:274)
            at org.apache.hive.service.cli.operation.Operation.run(Operation.java:337)
            at org.apache.hive.service.cli.session.HiveSessionImpl.executeStatementInternal(HiveSessionImpl.java:439)
            at org.apache.hive.service.cli.session.HiveSessionImpl.executeStatement(HiveSessionImpl.java:405)
            at sun.reflect.GeneratedMethodAccessor65.invoke(Unknown Source)
            at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
            at java.lang.reflect.Method.invoke(Method.java:606)
            at org.apache.hive.service.cli.session.HiveSessionProxy.invoke(HiveSessionProxy.java:78)
            at org.apache.hive.service.cli.session.HiveSessionProxy.access$000(HiveSessionProxy.java:36)
            at org.apache.hive.service.cli.session.HiveSessionProxy$1.run(HiveSessionProxy.java:63)
            at java.security.AccessController.doPrivileged(Native Method)
            at javax.security.auth.Subject.doAs(Subject.java:415)
            at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1920)
            at org.apache.hive.service.cli.session.HiveSessionProxy.invoke(HiveSessionProxy.java:59)
            at com.sun.proxy.$Proxy28.executeStatement(Unknown Source)
            at org.apache.hive.service.cli.CLIService.executeStatement(CLIService.java:257)
            at org.apache.hive.service.cli.thrift.ThriftCLIService.ExecuteStatement(ThriftCLIService.java:501)
            at org.apache.hive.service.cli.thrift.TCLIService$Processor$ExecuteStatement.getResult(TCLIService.java:1313)
            at org.apache.hive.service.cli.thrift.TCLIService$Processor$ExecuteStatement.getResult(TCLIService.java:1298)
            at org.apache.thrift.ProcessFunction.process(ProcessFunction.java:39)
            at org.apache.thrift.TBaseProcessor.process(TBaseProcessor.java:39)
            at org.apache.hive.service.auth.TSetIpAddressProcessor.process(TSetIpAddressProcessor.java:56)
            at org.apache.thrift.server.TThreadPoolServer$WorkerProcess.run(TThreadPoolServer.java:286)
            at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
            at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
            at java.lang.Thread.run(Thread.java:745)
    Caused by: java.io.IOException: error=13, Permission denied
            at java.lang.UNIXProcess.forkAndExec(Native Method)
            at java.lang.UNIXProcess.<init>(UNIXProcess.java:186)
            at java.lang.ProcessImpl.start(ProcessImpl.java:130)
            at java.lang.ProcessBuilder.start(ProcessBuilder.java:1028)
            ... 38 more
