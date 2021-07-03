import json

from pyjetbrainsdevecosystem.file_utils import unpack_csv_data, split_data_by_dash

questions_dict = {}
with open('survey_data/2017/DevEcosystem Survey 2016_2017 By JetBrains Questions.txt',
          encoding='utf8') as questions_text:
    for row in questions_text.readlines():
        question, description = split_data_by_dash(row, 2017)
        questions_dict.update({question: description})

question_column_map = {}
with open('survey_data/2017/DevEcosystem Survey 2016_2017 By JetBrains Raw Data.csv',
          newline='',
          encoding='utf8') as survey_text:
    survey_reader = unpack_csv_data(survey_text)
    survey_fieldnames = survey_reader.fieldnames
    for question in questions_dict.keys():
        field_list_with_position = {}
        for field_name in survey_fieldnames:
            if field_name.find(question) == 0:
                column_number = survey_fieldnames.index(field_name)
                field_list_with_position.update({field_name: column_number})
                question_column_map.update({question: field_list_with_position})


print(json.dumps(question_column_map, indent=4))
# {
#     "language": {
#         "language": 0
#     },
#     "channel": {
#         "channel": 1
#     },
#     "dev.environment": {
#         "dev.environment.Windows": 2,
#         "dev.environment.Unix / Linux": 3,
#         "dev.environment.macOS": 4,
#         "dev.environment.Other - Write In": 5
#     },
#     "app.type": {
#         "app.type.Web Back-end": 6,
#         "app.type.Web Front-end": 7,
#         "app.type.Mobile": 8,
#         "app.type.Desktop": 9,
#         "app.type.Enterprise Back-end Service": 10,
#         "app.type.Data analysis / BI": 11,
#         "app.type.Embedded / IoT": 12,
#         "app.type.Other - Write In": 13
#     },
#     "mobile.os": {
#         "mobile.os.Windows": 14,
#         "mobile.os.Android": 15,
#         "mobile.os.iOS": 16,
#         "mobile.os.Other - Write In": 17
#     },
#     "desktop.os": {
#         "desktop.os.Windows": 18,
#         "desktop.os.Unix / Linux": 19,
#         "desktop.os.macOS": 20,
#         "desktop.os.Other - Write In": 21
#     },
#     "programming.language": {
#         "programming.language.Java": 22,
#         "programming.language.C": 23,
#         "programming.language.C++": 24,
#         "programming.language.Python": 25,
#         "programming.language.C#": 26,
#         "programming.language.PHP": 27,
#         "programming.language.JavaScript": 28,
#         "programming.language.Ruby": 29,
#         "programming.language.Elixir": 30,
#         "programming.language.Crystal": 31,
#         "programming.language.Kotlin": 32,
#         "programming.language.Swift": 33,
#         "programming.language.Objective-C": 34,
#         "programming.language.Visual Basic": 35,
#         "programming.language.Scala": 36,
#         "programming.language.Go": 37,
#         "programming.language.HTML / CSS": 38,
#         "programming.language.Haskell": 39,
#         "programming.language.R": 40,
#         "programming.language.SQL": 41,
#         "programming.language.TypeScript": 42,
#         "programming.language.Dart": 43,
#         "programming.language.CoffeeScript": 44,
#         "programming.language.Clojure / ClojureScript": 45,
#         "programming.language.Delphi": 46,
#         "programming.language.Cobol": 47,
#         "programming.language.Groovy": 48,
#         "programming.language.Other - Write In": 49,
#         "programming.language.migrate.Java": 50,
#         "programming.language.migrate.C": 51,
#         "programming.language.migrate.C++": 52,
#         "programming.language.migrate.Python": 53,
#         "programming.language.migrate.C#": 54,
#         "programming.language.migrate.PHP": 55,
#         "programming.language.migrate.JavaScript": 56,
#         "programming.language.migrate.Ruby": 57,
#         "programming.language.migrate.Elixir": 58,
#         "programming.language.migrate.Crystal": 59,
#         "programming.language.migrate.Kotlin": 60,
#         "programming.language.migrate.Swift": 61,
#         "programming.language.migrate.Objective-C": 62,
#         "programming.language.migrate.Visual Basic": 63,
#         "programming.language.migrate.Scala": 64,
#         "programming.language.migrate.Go": 65,
#         "programming.language.migrate.HTML / CSS": 66,
#         "programming.language.migrate.Haskell": 67,
#         "programming.language.migrate.R": 68,
#         "programming.language.migrate.SQL": 69,
#         "programming.language.migrate.TypeScript": 70,
#         "programming.language.migrate.Dart": 71,
#         "programming.language.migrate.CoffeeScript": 72,
#         "programming.language.migrate.Clojure / ClojureScript": 73,
#         "programming.language.migrate.Delphi": 74,
#         "programming.language.migrate.Cobol": 75,
#         "programming.language.migrate.Groovy": 76,
#         "programming.language.migrate.Planning to adopt / migrate to other language(s) - Write in": 77,
#         "programming.language.migrate.No, not planning to adopt / migrate": 78,
#         "programming.language.primary": 79
#     },
#     "programming.language.migrate": {
#         "programming.language.migrate.Java": 50,
#         "programming.language.migrate.C": 51,
#         "programming.language.migrate.C++": 52,
#         "programming.language.migrate.Python": 53,
#         "programming.language.migrate.C#": 54,
#         "programming.language.migrate.PHP": 55,
#         "programming.language.migrate.JavaScript": 56,
#         "programming.language.migrate.Ruby": 57,
#         "programming.language.migrate.Elixir": 58,
#         "programming.language.migrate.Crystal": 59,
#         "programming.language.migrate.Kotlin": 60,
#         "programming.language.migrate.Swift": 61,
#         "programming.language.migrate.Objective-C": 62,
#         "programming.language.migrate.Visual Basic": 63,
#         "programming.language.migrate.Scala": 64,
#         "programming.language.migrate.Go": 65,
#         "programming.language.migrate.HTML / CSS": 66,
#         "programming.language.migrate.Haskell": 67,
#         "programming.language.migrate.R": 68,
#         "programming.language.migrate.SQL": 69,
#         "programming.language.migrate.TypeScript": 70,
#         "programming.language.migrate.Dart": 71,
#         "programming.language.migrate.CoffeeScript": 72,
#         "programming.language.migrate.Clojure / ClojureScript": 73,
#         "programming.language.migrate.Delphi": 74,
#         "programming.language.migrate.Cobol": 75,
#         "programming.language.migrate.Groovy": 76,
#         "programming.language.migrate.Planning to adopt / migrate to other language(s) - Write in": 77,
#         "programming.language.migrate.No, not planning to adopt / migrate": 78
#     },
#     "programming.language.primary": {
#         "programming.language.primary": 79
#     },
#     "unit.testing": {
#         "unit.testing": 80
#     },
#     "database": {
#         "database.None": 81,
#         "database.DB2": 82,
#         "database.MS SQL Server": 83,
#         "database.MySQL": 84,
#         "database.Oracle Database": 85,
#         "database.PostgreSQL": 86,
#         "database.SQLite": 87,
#         "database.Cassandra": 88,
#         "database.Couchbase": 89,
#         "database.HBase": 90,
#         "database.MongoDB": 91,
#         "database.Neo4j": 92,
#         "database.Redis": 93,
#         "database.other": 94,
#         "database.migrate.DB2": 95,
#         "database.migrate.MS SQL Server": 96,
#         "database.migrate.SQLite": 97,
#         "database.migrate.Oracle Database": 98,
#         "database.migrate.PostgreSQL": 99,
#         "database.migrate.MySQL": 100,
#         "database.migrate.MongoDB": 101,
#         "database.migrate.Redis": 102,
#         "database.migrate.Cassandra": 103,
#         "database.migrate.HBase": 104,
#         "database.migrate.Neo4j": 105,
#         "database.migrate.Couchbase": 106,
#         "database.migrate.Yes, planning to adopt / migrate to other database(s) - Write in": 107,
#         "database.migrate.No, not planning to adopt / migrate": 108,
#         "database.host.Locally": 109,
#         "database.host.Private Servers": 110,
#         "database.host.Amazon Web Services": 111,
#         "database.host.Microsoft Azure": 112,
#         "database.host.Google Cloud Platform": 113,
#         "database.host.Rackspace": 114,
#         "database.host.RedHat OpenShift": 115,
#         "database.host.IBM SoftLayer": 116,
#         "database.host.Cloud Foundry": 117,
#         "database.host.Heroku": 118,
#         "database.host.Other - Write In": 119
#     },
#     "database.migrate": {
#         "database.migrate.DB2": 95,
#         "database.migrate.MS SQL Server": 96,
#         "database.migrate.SQLite": 97,
#         "database.migrate.Oracle Database": 98,
#         "database.migrate.PostgreSQL": 99,
#         "database.migrate.MySQL": 100,
#         "database.migrate.MongoDB": 101,
#         "database.migrate.Redis": 102,
#         "database.migrate.Cassandra": 103,
#         "database.migrate.HBase": 104,
#         "database.migrate.Neo4j": 105,
#         "database.migrate.Couchbase": 106,
#         "database.migrate.Yes, planning to adopt / migrate to other database(s) - Write in": 107,
#         "database.migrate.No, not planning to adopt / migrate": 108
#     },
#     "database.host": {
#         "database.host.Locally": 109,
#         "database.host.Private Servers": 110,
#         "database.host.Amazon Web Services": 111,
#         "database.host.Microsoft Azure": 112,
#         "database.host.Google Cloud Platform": 113,
#         "database.host.Rackspace": 114,
#         "database.host.RedHat OpenShift": 115,
#         "database.host.IBM SoftLayer": 116,
#         "database.host.Cloud Foundry": 117,
#         "database.host.Heroku": 118,
#         "database.host.Other - Write In": 119
#     },
#     "tool.usage": {
#         "tool.usage.Source code collaboration tool (e.g. GitHub, GitLab, Bitbucket)": 120,
#         "tool.usage.Issue tracker (e.g. JIRA, YouTrack)": 121,
#         "tool.usage.Code review tool (e.g. Crucible, Upsource)": 122,
#         "tool.usage.Continuous Integration (CI) tool (e.g. Travis, Jenkins)": 123,
#         "tool.usage.Static analysis tool (e.g. CodeClimate)": 124,
#         "tool.usage.IDE (e.g. Eclipse, IntelliJ IDEA)": 125,
#         "tool.usage.Lightweight Desktop Editor (e.g. Sublime Text, Atom, VS Code, Vim)": 126,
#         "tool.usage.In-cloud Editor or IDE": 127
#     },
#     "team.adopted": {
#         "team.adopted.Source code collaboration tool (e.g. GitHub, GitLab, BitBucket)": 128,
#         "team.adopted.Issue tracker (e.g. JIRA, YouTrack)": 129,
#         "team.adopted.Code review tool (e.g. Crucible, Upsource)": 130,
#         "team.adopted.Continuous Integration (CI) tool (e.g. Travis, Jenkins)": 131,
#         "team.adopted.Static analysis tool (e.g. CodeClimate)": 132,
#         "team.adopted.IDE (e.g. Eclipse, IntelliJ IDEA)": 133,
#         "team.adopted.None of the above": 134
#     },
#     "ci": {
#         "ci.Jenkins / Hudson": 135,
#         "ci.TeamCity": 136,
#         "ci.Bamboo": 137,
#         "ci.Microsoft Team Foundation Build": 138,
#         "ci.Travis CI": 139,
#         "ci.Codeship": 140,
#         "ci.CircleCI": 141,
#         "ci.CruiseControl": 142,
#         "ci.GoCD": 143,
#         "ci.Gitlab CI": 144,
#         "ci.Other - Write In": 145
#     },
#     "issue.tracker": {
#         "issue.tracker.JIRA": 146,
#         "issue.tracker.YouTrack": 147,
#         "issue.tracker.Redmine": 148,
#         "issue.tracker.GitLab Issue Board": 149,
#         "issue.tracker.Asana": 150,
#         "issue.tracker.Wrike": 151,
#         "issue.tracker.Microsoft TFS": 152,
#         "issue.tracker.Trello": 153,
#         "issue.tracker.GitHub Issues": 154,
#         "issue.tracker.Other - Write In": 155
#     },
#     "use.in.cloud": {
#         "use.in.cloud.None": 156,
#         "use.in.cloud.Continuous Integration Tool": 157,
#         "use.in.cloud.Code Review Tool": 158,
#         "use.in.cloud.Issue Tracker": 159
#     },
#     "version.control.system": {
#         "version.control.system.None": 160,
#         "version.control.system.Concurrent Versions System (CVS)": 161,
#         "version.control.system.Apache Subversion (SVN)": 162,
#         "version.control.system.Git": 163,
#         "version.control.system.Mercurial": 164,
#         "version.control.system.Bazaar": 165,
#         "version.control.system.Perforce": 166,
#         "version.control.system.Other - Write In": 167
#     },
#     "where.keep.code": {
#         "where.keep.code.Version control as a service (e.g. GitHub, Bitbucket)": 168,
#         "where.keep.code.Manually deployed version control (e.g. GitHub Enterprise, GitLab)": 169,
#         "where.keep.code.Other - Write In": 170
#     },
#     "version.control.service": {
#         "version.control.service.None": 171,
#         "version.control.service.GitHub": 172,
#         "version.control.service.GitLab": 173,
#         "version.control.service.Bitbucket": 174,
#         "version.control.service.Gitcolony": 175,
#         "version.control.service.Perforce": 176,
#         "version.control.service.Amazon CodeCommit": 177,
#         "version.control.service.RhodeCode": 178,
#         "version.control.service.SourceForge": 179,
#         "version.control.service.Custom tool": 180,
#         "version.control.service.Other - Write In": 181
#     },
#     "ide.how.often": {
#         "ide.how.often.How often do you usually use your IDE?": 182
#     },
#     "customise.ide": {
#         "customise.ide.No, I don't customize": 183,
#         "customise.ide.Yes, I use custom color schemes": 184,
#         "customise.ide.Yes, I use custom keymaps": 185,
#         "customise.ide.Yes, I use plugins": 186,
#         "customise.ide.Other - Write In": 187
#     },
#     "invesitgations": {
#         "invesitgations.None": 188,
#         "invesitgations.Exception analysis": 189,
#         "invesitgations.Performance analysis (bottlenecks, algorithm optimizations, etc.)": 190,
#         "invesitgations.Memory analysis (memory distribution, traffic, leaks, etc.)": 191,
#         "invesitgations.Concurrency analysis (race conditions, wait analysis, deadlocks, CPU scheduling, etc.)": 192,
#         "invesitgations.Application crash analysis": 193,
#         "invesitgations.Other - Write In": 194
#     },
#     "diagnostic": {
#         "diagnostic.None": 195,
#         "diagnostic.Debugging": 196,
#         "diagnostic.CPU profiling": 197,
#         "diagnostic.Memory profiling": 198,
#         "diagnostic.Database profiling": 199,
#         "diagnostic.GPU profiling": 200,
#         "diagnostic.Logging": 201,
#         "diagnostic.Collecting thread dumps": 202,
#         "diagnostic.Timeline visualization": 203,
#         "diagnostic.Events Tracing for Windows (ETW)": 204,
#         "diagnostic.Other - Write In": 205
#     },
#     "video.games": {
#         "video.games": 206,
#         "video.games.genre": 207
#     },
#     "video.games.genre": {
#         "video.games.genre": 207
#     },
#     "java.version": {
#         "java.version.Java 8": 208,
#         "java.version.Java 7": 209,
#         "java.version.Java 6": 210,
#         "java.version.Other - Write In": 211
#     },
#     "java.app.server": {
#         "java.app.server.None": 212,
#         "java.app.server.Apache Tomcat": 213,
#         "java.app.server.Jetty": 214,
#         "java.app.server.Wildfly": 215,
#         "java.app.server.JBoss EAP": 216,
#         "java.app.server.Weblogic": 217,
#         "java.app.server.WebSphere": 218,
#         "java.app.server.Glassfish": 219,
#         "java.app.server.Other - Write In": 220
#     },
#     "java.framework.app.server": {
#         "java.framework.app.server.None": 221,
#         "java.framework.app.server.Netty": 222,
#         "java.framework.app.server.Undertow": 223,
#         "java.framework.app.server.Vert.x": 224,
#         "java.framework.app.server.Spark Java": 225,
#         "java.framework.app.server.Other - Write In": 226
#     },
#     "java.deploy": {
#         "java.deploy.As artifacts (e.g. WAR)": 227,
#         "java.deploy.I use an embedded server (e.g. JAR)": 228,
#         "java.deploy.I'm not sure": 229
#     },
#     "java.web.framework": {
#         "java.web.framework.No, I don't use any": 230,
#         "java.web.framework.Spring MVC": 231,
#         "java.web.framework.GWT": 232,
#         "java.web.framework.Vaadin": 233,
#         "java.web.framework.Play Framework": 234,
#         "java.web.framework.Grails 2": 235,
#         "java.web.framework.Grails 3": 236,
#         "java.web.framework.Spring Boot": 237,
#         "java.web.framework.JSF": 238,
#         "java.web.framework.Struts 1": 239,
#         "java.web.framework.Struts 2": 240,
#         "java.web.framework.Wicket": 241,
#         "java.web.framework.Dropwizard": 242,
#         "java.web.framework.Other - Write In": 243
#     },
#     "java.build.system": {
#         "java.build.system.None": 244,
#         "java.build.system.Maven": 245,
#         "java.build.system.SBT": 246,
#         "java.build.system.Gradle": 247,
#         "java.build.system.Ant": 248,
#         "java.build.system.Other - Write In": 249
#     },
#     "java.ee.version": {
#         "java.ee.version.None": 250,
#         "java.ee.version.Java EE 7": 251,
#         "java.ee.version.Java EE 6": 252,
#         "java.ee.version.Java EE 5": 253,
#         "java.ee.version.J2SE": 254,
#         "java.ee.version.Other - Write In": 255
#     },
#     "java.jvm.profiler": {
#         "java.jvm.profiler.None": 256,
#         "java.jvm.profiler.VisualVM": 257,
#         "java.jvm.profiler.JProfiler": 258,
#         "java.jvm.profiler.Java Mission Control": 259,
#         "java.jvm.profiler.YourKit": 260,
#         "java.jvm.profiler.NetBeans profiler": 261,
#         "java.jvm.profiler.Our own custom tools": 262,
#         "java.jvm.profiler.Other - Write In": 263
#     },
#     "java.ide": {
#         "java.ide": 264
#     },
#     "c.standart": {
#         "c.standart.C99": 265,
#         "c.standart.C11": 266,
#         "c.standart.Embedded C": 267,
#         "c.standart.Other - Write In": 268
#     },
#     "c.ide": {
#         "c.ide": 269
#     },
#     "c.unit.testing": {
#         "c.unit.testing.None": 270,
#         "c.unit.testing.Catch": 271,
#         "c.unit.testing.Boost.Test": 272,
#         "c.unit.testing.Google Test": 273,
#         "c.unit.testing.CppUnit": 274,
#         "c.unit.testing.CppUTest": 275,
#         "c.unit.testing.Other - Write In": 276
#     },
#     "c.project.model": {
#         "c.project.model.None": 277,
#         "c.project.model.Visual Studio project": 278,
#         "c.project.model.Xcode project": 279,
#         "c.project.model.Autotools": 280,
#         "c.project.model.Makefiles": 281,
#         "c.project.model.CMake": 282,
#         "c.project.model.Qmake": 283,
#         "c.project.model.SCons": 284,
#         "c.project.model.Boost.Build": 285,
#         "c.project.model.Basel": 286,
#         "c.project.model.Custom": 287,
#         "c.project.model.Other - Write In": 288
#     },
#     "c.compiler": {
#         "c.compiler.GCC": 289,
#         "c.compiler.Clang": 290,
#         "c.compiler.MSVC": 291,
#         "c.compiler.Intel": 292,
#         "c.compiler.Custom": 293,
#         "c.compiler.Other - Write In": 294
#     },
#     "cpp.standart": {
#         "cpp.standart.C++98": 295,
#         "cpp.standart.C++03": 296,
#         "cpp.standart.C++11": 297,
#         "cpp.standart.C++14": 298,
#         "cpp.standart.C++17": 299,
#         "cpp.standart.migrate": 300
#     },
#     "cpp.standart.migrate": {
#         "cpp.standart.migrate": 300
#     },
#     "cpp.cli": {
#         "cpp.cli": 301
#     },
#     "cpp.ide": {
#         "cpp.ide": 302
#     },
#     "cpp.unit.testing": {
#         "cpp.unit.testing.None": 303,
#         "cpp.unit.testing.Boost.Test": 304,
#         "cpp.unit.testing.Google Test": 305,
#         "cpp.unit.testing.CppUnit": 306,
#         "cpp.unit.testing.CppUTest": 307,
#         "cpp.unit.testing.Catch": 308,
#         "cpp.unit.testing.Other - Write In": 309
#     },
#     "cpp.project.model": {
#         "cpp.project.model.None": 310,
#         "cpp.project.model.Visual Studio project": 311,
#         "cpp.project.model.Xcode project": 312,
#         "cpp.project.model.Autotools": 313,
#         "cpp.project.model.Makefiles": 314,
#         "cpp.project.model.CMake": 315,
#         "cpp.project.model.Qmake": 316,
#         "cpp.project.model.SCons": 317,
#         "cpp.project.model.Boost.Build": 318,
#         "cpp.project.model.Basel": 319,
#         "cpp.project.model.Custom": 320,
#         "cpp.project.model.Other - Write In": 321
#     },
#     "cpp.compiler": {
#         "cpp.compiler.GCC": 322,
#         "cpp.compiler.Clang": 323,
#         "cpp.compiler.MSVC": 324,
#         "cpp.compiler.Intel": 325,
#         "cpp.compiler.Custom": 326,
#         "cpp.compiler.Other - Write In": 327
#     },
#     "cpp.project.size": {
#         "cpp.project.size": 328
#     },
#     "python.version": {
#         "python.version": 329
#     },
#     "python.techs": {
#         "python.techs.Anaconda / NumPy / matpoltlib / SciPy / Pandas and similar": 330,
#         "python.techs.Django": 331,
#         "python.techs.Flask": 332,
#         "python.techs.PyQT/PyGTK/wxPython": 333,
#         "python.techs.TkInter": 334,
#         "python.techs.SQLAlchemy": 335,
#         "python.techs.Pygame": 336,
#         "python.techs.Pillow": 337,
#         "python.techs.Sphinx": 338,
#         "python.techs.Web2py": 339,
#         "python.techs.Tornado": 340,
#         "python.techs.Bottle": 341,
#         "python.techs.Kivy": 342,
#         "python.techs.CherryPy": 343,
#         "python.techs.Pyramid": 344,
#         "python.techs.Other - Write In": 345
#     },
#     "python.ide": {
#         "python.ide": 346
#     },
#     "python.how.often": {
#         "python.how.often.Use autocompletion in your editor": 347,
#         "python.how.often.Use the debugger": 348,
#         "python.how.often.Refactor your code": 349,
#         "python.how.often.Use VCS": 350,
#         "python.how.often.Use code linting (programs that analyze code for potential errors)": 351,
#         "python.how.often.Use Python virtual environments for your projects": 352,
#         "python.how.often.Use databases and SQL": 353,
#         "python.how.often.Run / debug or edit code on remote machines (remote hosts, VMs, etc.)": 354,
#         "python.how.often.Use Python profiler": 355,
#         "python.how.often.Write tests for your code": 356,
#         "python.how.often.Use code coverage": 357
#     },
#     "csharp.version": {
#         "csharp.version.C# 5": 358,
#         "csharp.version.C# 6": 359,
#         "csharp.version.C# 7": 360,
#         "csharp.version.Earlier version": 361,
#         "csharp.version.I'm not sure": 362
#     },
#     "csharp.runtime": {
#         "csharp.runtime..NET Framework": 363,
#         "csharp.runtime.Mono": 364,
#         "csharp.runtime..NET Core": 365
#     },
#     "csharp.framework": {
#         "csharp.framework.None": 366,
#         "csharp.framework.Sharepoint": 367,
#         "csharp.framework.ASP.NET MVC": 368,
#         "csharp.framework.ASP.NET Web Forms": 369,
#         "csharp.framework.ASP.NET Core": 370,
#         "csharp.framework.Windows Presentation Foundation (WPF)": 371,
#         "csharp.framework.Windows Forms": 372,
#         "csharp.framework.Windows Communication Foundation (WCF)": 373,
#         "csharp.framework.Entity Framework": 374,
#         "csharp.framework.Unity3d": 375,
#         "csharp.framework.Xamarin": 376,
#         "csharp.framework.UWP": 377,
#         "csharp.framework.Other - Write In": 378
#     },
#     "csharp.ide": {
#         "csharp.ide": 379
#     },
#     "csharp.visual.studio.version": {
#         "csharp.visual.studio.version": 380
#     },
#     "csharp.unit.testing": {
#         "csharp.unit.testing.None": 381,
#         "csharp.unit.testing.MSTest/Visual Studio Unit Testing Framework": 382,
#         "csharp.unit.testing.NUnit": 383,
#         "csharp.unit.testing.xUnit": 384,
#         "csharp.unit.testing.MbUnit": 385,
#         "csharp.unit.testing.Other - Write In": 386
#     },
#     "csharp.tools": {
#         "csharp.tools.None": 387,
#         "csharp.tools.YourKit Profiler": 388,
#         "csharp.tools.Windows Performance Toolkit": 389,
#         "csharp.tools.Visual Studio's built-in performance and diagnostic tools": 390,
#         "csharp.tools.dotTrace": 391,
#         "csharp.tools.dotMemory": 392,
#         "csharp.tools.ANTS Profiler": 393,
#         "csharp.tools.Other - Write In": 394
#     },
#     "php.version": {
#         "php.version": 395
#     },
#     "php.environtment": {
#         "php.environtment.Local environment": 396,
#         "php.environtment.Remote environment (SFTP, SSH, Remote desktop, etc.)": 397,
#         "php.environtment.Virtualized environment (Vagrant, Otto, etc.)": 398,
#         "php.environtment.Containerized environment (Docker, Rocket)": 399,
#         "php.environtment.Other - Write In": 400
#     },
#     "php.debugger": {
#         "php.debugger": 401
#     },
#     "php.frameworks": {
#         "php.frameworks.None": 402,
#         "php.frameworks.Symfony": 403,
#         "php.frameworks.Drupal": 404,
#         "php.frameworks.WordPress": 405,
#         "php.frameworks.Zend": 406,
#         "php.frameworks.Magento": 407,
#         "php.frameworks.Laravel": 408,
#         "php.frameworks.Joomla!": 409,
#         "php.frameworks.Yii": 410,
#         "php.frameworks.CakePHP": 411,
#         "php.frameworks.Other - Write In": 412
#     },
#     "php.ide": {
#         "php.ide.Aptana": 413,
#         "php.ide.Atom": 414,
#         "php.ide.BBEdit": 415,
#         "php.ide.Coda": 416,
#         "php.ide.Eclipse PDT": 417,
#         "php.ide.Komodo IDE": 418,
#         "php.ide.NetBeans IDE": 419,
#         "php.ide.Notepad++": 420,
#         "php.ide.PHPEdit": 421,
#         "php.ide.PhpStorm": 422,
#         "php.ide.Sublime Text": 423,
#         "php.ide.Vim": 424,
#         "php.ide.Zend Studio": 425,
#         "php.ide.Other - Write In": 426
#     },
#     "php.unit.testing": {
#         "php.unit.testing.None": 427,
#         "php.unit.testing.PHPUnit": 428,
#         "php.unit.testing.Behat": 429,
#         "php.unit.testing.PHPSpec": 430,
#         "php.unit.testing.Codeception": 431,
#         "php.unit.testing.SimpleTest": 432,
#         "php.unit.testing.Other - Write In": 433
#     },
#     "kotlin.library": {
#         "kotlin.library.None": 434,
#         "kotlin.library.Kotlin Android Extensions": 435,
#         "kotlin.library.RxKotlin": 436,
#         "kotlin.library.Anko": 437,
#         "kotlin.library.Kotlinx": 438,
#         "kotlin.library.Kotter Knife": 439,
#         "kotlin.library.Anko (DSL)": 440,
#         "kotlin.library.KotlinTest": 441,
#         "kotlin.library.Spek": 442,
#         "kotlin.library.Kotson": 443,
#         "kotlin.library.Kovenant": 444,
#         "kotlin.library.Kodein": 445,
#         "kotlin.library.Fuel": 446,
#         "kotlin.library.TornadoFX": 447,
#         "kotlin.library.HamKrest": 448,
#         "kotlin.library.Other - Write In": 449
#     },
#     "ruby.version": {
#         "ruby.version": 450,
#         "ruby.version.migrate": 451,
#         "ruby.version.manager.None": 452,
#         "ruby.version.manager.RVM": 453,
#         "ruby.version.manager.Rbenv": 454,
#         "ruby.version.manager.Ruby-build": 455,
#         "ruby.version.manager.Chruby": 456,
#         "ruby.version.manager.Other - Write In": 457
#     },
#     "ruby.version.migrate": {
#         "ruby.version.migrate": 451
#     },
#     "ruby.version.manager": {
#         "ruby.version.manager.None": 452,
#         "ruby.version.manager.RVM": 453,
#         "ruby.version.manager.Rbenv": 454,
#         "ruby.version.manager.Ruby-build": 455,
#         "ruby.version.manager.Chruby": 456,
#         "ruby.version.manager.Other - Write In": 457
#     },
#     "ruby.gem.management": {
#         "ruby.gem.management.None": 458,
#         "ruby.gem.management.Bundler": 459,
#         "ruby.gem.management.RVM gemsets": 460,
#         "ruby.gem.management.Rbenv gemsets": 461,
#         "ruby.gem.management.Other - Write In": 462
#     },
#     "ruby.gems.count": {
#         "ruby.gems.count": 463
#     },
#     "ruby.framework": {
#         "ruby.framework.None": 464,
#         "ruby.framework.Ruby on Rails": 465,
#         "ruby.framework.Rack": 466,
#         "ruby.framework.Sinatra": 467,
#         "ruby.framework.Padrino": 468,
#         "ruby.framework.Cramp": 469,
#         "ruby.framework.Cuba": 470,
#         "ruby.framework.Hanami": 471,
#         "ruby.framework.React.rb": 472,
#         "ruby.framework.Opal": 473,
#         "ruby.framework.Other - Write": 474
#     },
#     "ruby.rails.version": {
#         "ruby.rails.version": 475,
#         "ruby.rails.version.migrate": 476
#     },
#     "ruby.rails.version.migrate": {
#         "ruby.rails.version.migrate": 476
#     },
#     "ruby.server": {
#         "ruby.server.None": 477,
#         "ruby.server.Unicorn": 478,
#         "ruby.server.Puma": 479,
#         "ruby.server.Passenger (mod_rails)": 480,
#         "ruby.server.Thin": 481,
#         "ruby.server.Mongrel": 482,
#         "ruby.server.FastCGI": 483,
#         "ruby.server.Rainbows!": 484,
#         "ruby.server.Other - Write In": 485
#     },
#     "ruby.ide": {
#         "ruby.ide.RubyMine": 486,
#         "ruby.ide.IntelliJ IDEA with Ruby plugin (or other JetBrains IDEs)": 487,
#         "ruby.ide.Sublime Text": 488,
#         "ruby.ide.Vim": 489,
#         "ruby.ide.Atom": 490,
#         "ruby.ide.TextMate": 491,
#         "ruby.ide.Emacs": 492,
#         "ruby.ide.VS Code": 493,
#         "ruby.ide.Notepad++": 494,
#         "ruby.ide.Gedit": 495,
#         "ruby.ide.Other - Write In": 496,
#         "ruby.ide.collegues.None, I'm the only Ruby developer": 497,
#         "ruby.ide.collegues.RubyMine": 498,
#         "ruby.ide.collegues.IntelliJ IDEA with Ruby plugin (or other JetBrains IDEs)": 499,
#         "ruby.ide.collegues.Sublime Text": 500,
#         "ruby.ide.collegues.Vim": 501,
#         "ruby.ide.collegues.Atom": 502,
#         "ruby.ide.collegues.TextMate": 503,
#         "ruby.ide.collegues.Emacs": 504,
#         "ruby.ide.collegues.VS Code": 505,
#         "ruby.ide.collegues.Notepad++": 506,
#         "ruby.ide.collegues.Gedit": 507,
#         "ruby.ide.collegues.Other - Write In": 508
#     },
#     "ruby.ide.collegues": {
#         "ruby.ide.collegues.None, I'm the only Ruby developer": 497,
#         "ruby.ide.collegues.RubyMine": 498,
#         "ruby.ide.collegues.IntelliJ IDEA with Ruby plugin (or other JetBrains IDEs)": 499,
#         "ruby.ide.collegues.Sublime Text": 500,
#         "ruby.ide.collegues.Vim": 501,
#         "ruby.ide.collegues.Atom": 502,
#         "ruby.ide.collegues.TextMate": 503,
#         "ruby.ide.collegues.Emacs": 504,
#         "ruby.ide.collegues.VS Code": 505,
#         "ruby.ide.collegues.Notepad++": 506,
#         "ruby.ide.collegues.Gedit": 507,
#         "ruby.ide.collegues.Other - Write In": 508
#     },
#     "ruby.unit.testing": {
#         "ruby.unit.testing.None": 509,
#         "ruby.unit.testing.Shoulda": 510,
#         "ruby.unit.testing.Rspec": 511,
#         "ruby.unit.testing.Cucumber": 512,
#         "ruby.unit.testing.Minitest": 513,
#         "ruby.unit.testing.Test": 514,
#         "ruby.unit.testing.Other - Write In": 515
#     },
#     "swift.version": {
#         "swift.version": 516,
#         "swift.version.migrate": 517
#     },
#     "swift.version.migrate": {
#         "swift.version.migrate": 517
#     },
#     "swift.ide": {
#         "swift.ide": 518
#     },
#     "swift.unit.testing": {
#         "swift.unit.testing.None": 519,
#         "swift.unit.testing.XCTest": 520,
#         "swift.unit.testing.Quick + Nimble": 521,
#         "swift.unit.testing.KIF": 522,
#         "swift.unit.testing.Other - Write In": 523
#     },
#     "swift.ui.tests": {
#         "swift.ui.tests": 524
#     },
#     "swift.dependency.manager": {
#         "swift.dependency.manager": 525
#     },
#     "swift.database": {
#         "swift.database": 526
#     },
#     "swift.build.system": {
#         "swift.build.system": 527
#     },
#     "swift.linux": {
#         "swift.linux": 528
#     },
#     "objectivec.ide": {
#         "objectivec.ide": 529
#     },
#     "objectivec.unit.testing": {
#         "objectivec.unit.testing.None": 530,
#         "objectivec.unit.testing.XCTest": 531,
#         "objectivec.unit.testing.Google tests": 532,
#         "objectivec.unit.testing.Kiwi": 533,
#         "objectivec.unit.testing.Specta": 534,
#         "objectivec.unit.testing.Cedar": 535,
#         "objectivec.unit.testing.Other - Write In": 536
#     },
#     "objectivec.mock": {
#         "objectivec.mock": 537
#     },
#     "objectivec.ui.tests": {
#         "objectivec.ui.tests": 538
#     },
#     "objectivec.dependency.manager": {
#         "objectivec.dependency.manager": 539
#     },
#     "objectivec.database": {
#         "objectivec.database": 540
#     },
#     "objectivec.build.system": {
#         "objectivec.build.system": 541
#     },
#     "scala.java.version": {
#         "scala.java.version.Java 8": 542,
#         "scala.java.version.Java 7": 543,
#         "scala.java.version.Java 6": 544,
#         "scala.java.version.Other - Write In": 545
#     },
#     "scala.app.server": {
#         "scala.app.server.None": 546,
#         "scala.app.server.Apache Tomcat": 547,
#         "scala.app.server.Jetty": 548,
#         "scala.app.server.Wildfly": 549,
#         "scala.app.server.JBoss EAP": 550,
#         "scala.app.server.Weblogic": 551,
#         "scala.app.server.WebSphere": 552,
#         "scala.app.server.Glassfish": 553,
#         "scala.app.server.Other - Write In": 554
#     },
#     "scala.framework.app.server": {
#         "scala.framework.app.server.None": 555,
#         "scala.framework.app.server.Netty": 556,
#         "scala.framework.app.server.Undertow": 557,
#         "scala.framework.app.server.Vert.x": 558,
#         "scala.framework.app.server.Spark Java": 559,
#         "scala.framework.app.server.Other - Write In": 560
#     },
#     "scala.deploy.web.apps": {
#         "scala.deploy.web.apps": 561
#     },
#     "scala.framework": {
#         "scala.framework.app.server.None": 555,
#         "scala.framework.app.server.Netty": 556,
#         "scala.framework.app.server.Undertow": 557,
#         "scala.framework.app.server.Vert.x": 558,
#         "scala.framework.app.server.Spark Java": 559,
#         "scala.framework.app.server.Other - Write In": 560,
#         "scala.framework.Akka": 562,
#         "scala.framework.Spark": 563,
#         "scala.framework.ScalaTest": 564,
#         "scala.framework.Scalaz": 565,
#         "scala.framework.Spray": 566,
#         "scala.framework.Scalacheck": 567,
#         "scala.framework.Specs2": 568,
#         "scala.framework.Shapeless": 569,
#         "scala.framework.Finagle": 570,
#         "scala.framework.Spring": 571,
#         "scala.framework.TestNG": 572,
#         "scala.framework.JUnit": 573,
#         "scala.framework.Cats": 574,
#         "scala.framework.Breeze": 575,
#         "scala.framework.Slick": 576,
#         "scala.framework.Scala.js": 577,
#         "scala.framework.Other - Write In": 578
#     },
#     "scala.ide": {
#         "scala.ide.Eclipse": 579,
#         "scala.ide.IntelliJ IDEA": 580,
#         "scala.ide.NetBeans": 581,
#         "scala.ide.Vim": 582,
#         "scala.ide.Sublime": 583,
#         "scala.ide.Atom": 584,
#         "scala.ide.Other - Write In": 585,
#         "scala.ide.rank.Eclipse": 586,
#         "scala.ide.rank.IntelliJ IDEA": 587,
#         "scala.ide.rank.Vim": 588,
#         "scala.ide.rank.Sublime": 589,
#         "scala.ide.rank.Atom": 590
#     },
#     "scala.ide.rank": {
#         "scala.ide.rank.Eclipse": 586,
#         "scala.ide.rank.IntelliJ IDEA": 587,
#         "scala.ide.rank.Vim": 588,
#         "scala.ide.rank.Sublime": 589,
#         "scala.ide.rank.Atom": 590
#     },
#     "scala.jvm.profiler": {
#         "scala.jvm.profiler.None": 591,
#         "scala.jvm.profiler.VisualVM": 592,
#         "scala.jvm.profiler.JProfiler": 593,
#         "scala.jvm.profiler.Java Mission Control": 594,
#         "scala.jvm.profiler.YourKit": 595,
#         "scala.jvm.profiler.NetBeans profiler": 596,
#         "scala.jvm.profiler.Our own custom tools": 597,
#         "scala.jvm.profiler.Other - Write In": 598
#     },
#     "scala.build.system": {
#         "scala.build.system.None": 599,
#         "scala.build.system.Maven": 600,
#         "scala.build.system.Gradle": 601,
#         "scala.build.system.Ant": 602,
#         "scala.build.system.SBT": 603,
#         "scala.build.system.Other - Write In": 604
#     },
#     "scala.macros": {
#         "scala.macros": 605
#     },
#     "javascript.ecma6": {
#         "javascript.ecma6": 606
#     },
#     "javascript.framework": {
#         "javascript.framework.None": 607,
#         "javascript.framework.AngularJS": 608,
#         "javascript.framework.Angular 2": 609,
#         "javascript.framework.React": 610,
#         "javascript.framework.React Native": 611,
#         "javascript.framework.Cordova / PhoneGap": 612,
#         "javascript.framework.Express": 613,
#         "javascript.framework.Vue.js": 614,
#         "javascript.framework.Meteor": 615,
#         "javascript.framework.Ember": 616,
#         "javascript.framework.Backbone": 617,
#         "javascript.framework.Aurelia": 618,
#         "javascript.framework.Polymer": 619,
#         "javascript.framework.Electron": 620,
#         "javascript.framework.Other - Write In": 621
#     },
#     "javascript.ide": {
#         "javascript.ide.WebStorm (or other JetBrains IDEs)": 622,
#         "javascript.ide.Sublime Text": 623,
#         "javascript.ide.Atom": 624,
#         "javascript.ide.VS Code": 625,
#         "javascript.ide.Vi / Vim": 626,
#         "javascript.ide.Visual Studio": 627,
#         "javascript.ide.NotePad++": 628,
#         "javascript.ide.Other - Write In": 629
#     },
#     "javascript.unit.testing": {
#         "javascript.unit.testing.None": 630,
#         "javascript.unit.testing.Mocha": 631,
#         "javascript.unit.testing.Jest": 632,
#         "javascript.unit.testing.Ava": 633,
#         "javascript.unit.testing.Karma": 634,
#         "javascript.unit.testing.Jasmine": 635,
#         "javascript.unit.testing.Other - Write In": 636
#     },
#     "javascript.module.loader": {
#         "javascript.module.loader.None": 637,
#         "javascript.module.loader.Browserify": 638,
#         "javascript.module.loader.Webpack": 639,
#         "javascript.module.loader.RequireJS": 640,
#         "javascript.module.loader.SystemJS": 641,
#         "javascript.module.loader.Rollup": 642,
#         "javascript.module.loader.Other - Write In": 643
#     },
#     "db.sql.server.version": {
#         "db.sql.server.version": 644
#     },
#     "db.oracle.version": {
#         "db.oracle.version": 645
#     },
#     "db.mysql.version": {
#         "db.mysql.version": 646
#     },
#     "db.postressql.version": {
#         "db.postressql.version": 647
#     },
#     "db.db2.version": {
#         "db.db2.version": 648
#     },
#     "db.sqlite.version": {
#         "db.sqlite.version": 649
#     },
#     "db.managing.tool": {
#         "db.managing.tool.MySQL Workbench": 650,
#         "db.managing.tool.pgAdmin": 651,
#         "db.managing.tool.Oracle SQL Developer": 652,
#         "db.managing.tool.SQL Server Management Studio": 653,
#         "db.managing.tool.DataGrip": 654,
#         "db.managing.tool.phpMyAdmin": 655,
#         "db.managing.tool.Navicat": 656,
#         "db.managing.tool.Toad": 657,
#         "db.managing.tool.EMS SQL Manager": 658,
#         "db.managing.tool.dbForge Studio": 659,
#         "db.managing.tool.HeidiSQL": 660,
#         "db.managing.tool.DbVisualizer": 661,
#         "db.managing.tool.DBeaver": 662,
#         "db.managing.tool.Sequel Pro": 663,
#         "db.managing.tool.SQuirreL SQL": 664,
#         "db.managing.tool.Command Line": 665,
#         "db.managing.tool.Other - Write In": 666
#     },
#     "sleep.hours": {
#         "sleep.hours": 667
#     },
#     "do.deployment": {
#         "do.deployment": 668
#     },
#     "deployment.configuration.management.tool": {
#         "deployment.configuration.management.tool.None": 669,
#         "deployment.configuration.management.tool.Puppet": 670,
#         "deployment.configuration.management.tool.Chef": 671,
#         "deployment.configuration.management.tool.Ansible": 672,
#         "deployment.configuration.management.tool.Salt": 673,
#         "deployment.configuration.management.tool.Other - Write In": 674
#     },
#     "do.static.analysis": {
#         "do.static.analysis": 675
#     },
#     "do.open.source": {
#         "do.open.source": 676
#     },
#     "coding.hours.job": {
#         "coding.hours.job": 677
#     },
#     "coding.hours.personal": {
#         "coding.hours.personal": 678
#     },
#     "coding.weekends": {
#         "coding.weekends": 679
#     },
#     "have.phone": {
#         "have.phone.No": 680,
#         "have.phone.Yes, Apple iOS": 681,
#         "have.phone.Yes, Android": 682,
#         "have.phone.Yes, Blackberry": 683,
#         "have.phone.Yes, Windows-based": 684,
#         "have.phone.Yes, Symbian": 685,
#         "have.phone.Yes, Other - Write In": 686
#     },
#     "visit.meetups": {
#         "visit.meetups": 687
#     },
#     "have.tried.intellij.based": {
#         "have.tried.intellij.based.IntelliJ IDEA": 688,
#         "have.tried.intellij.based.RubyMine": 689,
#         "have.tried.intellij.based.PyCharm": 690,
#         "have.tried.intellij.based.AppCode": 691,
#         "have.tried.intellij.based.CLion": 692,
#         "have.tried.intellij.based.PhpStorm": 693,
#         "have.tried.intellij.based.WebStorm": 694,
#         "have.tried.intellij.based.DataGrip": 695,
#         "have.tried.intellij.based.Rider": 696,
#         "have.tried.intellij.based.None": 697
#     },
#     "have.tried.dotnet": {
#         "have.tried.dotnet.ReSharper": 698,
#         "have.tried.dotnet.ReSharper C++": 699,
#         "have.tried.dotnet.dotCover": 700,
#         "have.tried.dotnet.dotTrace": 701,
#         "have.tried.dotnet.dotMemory": 702,
#         "have.tried.dotnet.dotPeek": 703,
#         "have.tried.dotnet.Rider": 704,
#         "have.tried.dotnet.None": 705
#     },
#     "have.tried.teamware": {
#         "have.tried.teamware.TeamCity": 706,
#         "have.tried.teamware.YouTrack": 707,
#         "have.tried.teamware.Upsource": 708,
#         "have.tried.teamware.Hub": 709,
#         "have.tried.teamware.None": 710
#     },
#     "have.tried.languages": {
#         "have.tried.languages.Kotlin": 711,
#         "have.tried.languages.MPS": 712,
#         "have.tried.languages.None": 713
#     },
#     "first.time.jetbrains": {
#         "first.time.jetbrains": 714
#     },
#     "recommend.jetbrains": {
#         "recommend.jetbrains": 715
#     },
#     "jetbrains.channels": {
#         "jetbrains.channels.None": 716,
#         "jetbrains.channels.Global twitter @jetbrains": 717,
#         "jetbrains.channels.Local twitter accounts (e.g. @jetbrains_de, @jetbrains_ru)": 718,
#         "jetbrains.channels.Product twitter accounts (e.g. @phpstorm, @resharper)": 719,
#         "jetbrains.channels.JetBrains company blog": 720,
#         "jetbrains.channels.JetBrains product blogs": 721,
#         "jetbrains.channels.JetBrains on Facebook": 722,
#         "jetbrains.channels.JetBrainsTV on YouTube": 723,
#         "jetbrains.channels.JetBrains official website, jetbrains.com": 724,
#         "jetbrains.channels.Other - Write In": 725
#     },
#     "keyboard.mouse": {
#         "keyboard.mouse": 726
#     },
#     "employment.status": {
#         "employment.status": 727
#     },
#     "job.role": {
#         "job.role.DBA": 728,
#         "job.role.Architect": 729,
#         "job.role.QA Engineer": 730,
#         "job.role.Developer / Programmer": 731,
#         "job.role.Technical support": 732,
#         "job.role.Data analyst": 733,
#         "job.role.Business analyst": 734,
#         "job.role.Team Lead": 735,
#         "job.role.Product Manager": 736,
#         "job.role.CIO / CEO / CTO": 737,
#         "job.role.Systems analyst": 738,
#         "job.role.Other - Write In": 739
#     },
#     "company.size": {
#         "company.size": 740
#     },
#     "company.industry": {
#         "company.industry": 741
#     },
#     "develop.for": {
#         "develop.for": 742
#     },
#     "primary.language.users.in.company": {
#         "primary.language.users.in.company": 743
#     },
#     "development.model": {
#         "development.model": 744
#     },
#     "it.experience": {
#         "it.experience": 745
#     },
#     "team.size": {
#         "team.size": 746
#     },
#     "primary.language.users.in.team": {
#         "primary.language.users.in.team": 747
#     },
#     "agile.framework": {
#         "agile.framework": 748
#     },
#     "company.education": {
#         "company.education.Company does not help with education": 749,
#         "company.education.Company hires coaches": 750,
#         "company.education.Company provides self-taught courses": 751,
#         "company.education.Company pays for external courses / training": 752,
#         "company.education.Fellow employees run internal courses": 753,
#         "company.education.Company pays for employees to attend industry conferences": 754,
#         "company.education.Other - Write In": 755
#     },
#     "do.advocate": {
#         "do.advocate": 756
#     },
#     "team.distributed": {
#         "team.distributed": 757
#     },
#     "ambidexterity": {
#         "ambidexterity": 758
#     },
#     "age": {
#         "age": 759
#     },
#     "country": {
#         "country": 760
#     }
# }
#
