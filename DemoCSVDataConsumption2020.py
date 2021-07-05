import json

from pyjetbrainsdevecosystem.data_import_utils import unpack_csv_data

questions_dict = {}
with open('survey_data/2020/DevEcosystem 2020 questions_outside.csv',
          encoding='utf8') as questions_text:
    questions_reader = unpack_csv_data(questions_text)
    questions_fieldnames = questions_reader.fieldnames
    for column in questions_reader:
        questions_dict.update(
            {
                column['shortname']:
                {
                    column['question_title'],
                    column['type'],
                    column['page'],
                    column['place']
                }
            }
        )

question_column_map = {}
with open('survey_data/2020/2020_sharing_data_outside.csv',
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

    entry_count = {}
    for response in survey_reader:
        response_data = {}
        question_row = question_column_map.items()
        for parent_question, column_name_dict in question_row:
            temp_dict = {}
            sub_entry_count = entry_count.get(parent_question, {})
            for column_name in column_name_dict:
                column_name: str
                temp_dict.update({column_name: response[column_name]})
                sub_entry_count[response[column_name]] = sub_entry_count.get(response[column_name], 0) + 1
            response_data.update({parent_question: temp_dict})
            entry_count.update({parent_question: sub_entry_count})
    print(json.dumps(entry_count, indent=4))

#print(json.dumps(question_column_map, indent=4))
# {
#     "os_devenv": {
#         "os_devenv.Windows": 19,
#         "os_devenv.Linux": 20,
#         "os_devenv.macOS": 21,
#         "os_devenv.Other": 22
#     },
#     "mobile_target_os": {
#         "mobile_target_os.Android": 1475,
#         "mobile_target_os.iOS": 1476,
#         "mobile_target_os.Other": 1477
#     },
#     "db_adopt": {
#         "db_adopt.No, I'm not planning to adopt / migrate to any": 242,
#         "db_adopt.Yes, I'm planning to adopt / migrate to other database(s) - Write In": 243,
#         "db_adopt.DB2": 244,
#         "db_adopt.MS SQL Server": 245,
#         "db_adopt.MySQL": 246,
#         "db_adopt.Oracle Database": 247,
#         "db_adopt.PostgreSQL": 248,
#         "db_adopt.SQLite": 249,
#         "db_adopt.Cassandra": 250,
#         "db_adopt.Couchbase": 251,
#         "db_adopt.HBase": 252,
#         "db_adopt.MongoDB": 253,
#         "db_adopt.Neo4j": 254,
#         "db_adopt.Redis": 255,
#         "db_adopt.Amazon Redshift": 256,
#         "db_adopt.H2": 257,
#         "db_adopt.MariaDB": 258,
#         "db_adopt.ClickHouse": 259,
#         "db_adopt.Other": 260
#     },
#     "proglang": {
#         "proglang.I don't use programming languages": 78,
#         "proglang.Java": 79,
#         "proglang.C": 80,
#         "proglang.C++": 81,
#         "proglang.Python": 82,
#         "proglang.C#": 83,
#         "proglang.PHP": 84,
#         "proglang.JavaScript": 85,
#         "proglang.Ruby": 86,
#         "proglang.Elixir": 87,
#         "proglang.Kotlin": 88,
#         "proglang.Swift": 89,
#         "proglang.Objective-C": 90,
#         "proglang.Visual Basic": 91,
#         "proglang.Scala": 92,
#         "proglang.Go": 93,
#         "proglang.HTML / CSS": 94,
#         "proglang.Haskell": 95,
#         "proglang.R": 96,
#         "proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 97,
#         "proglang.TypeScript": 98,
#         "proglang.Dart": 99,
#         "proglang.Clojure / ClojureScript": 100,
#         "proglang.Delphi": 101,
#         "proglang.Groovy": 102,
#         "proglang.Rust": 103,
#         "proglang.Perl": 104,
#         "proglang.Assembly": 105,
#         "proglang.Matlab": 106,
#         "proglang.Lua": 107,
#         "proglang.Shell scripting languages(bash/shell/powershell)": 108,
#         "proglang.Julia": 109,
#         "proglang.F#": 110,
#         "proglang.Other": 111,
#         "proglang_rank.Java": 183,
#         "proglang_rank.C": 184,
#         "proglang_rank.C++": 185,
#         "proglang_rank.Python": 186,
#         "proglang_rank.C#": 187,
#         "proglang_rank.PHP": 188,
#         "proglang_rank.JavaScript": 189,
#         "proglang_rank.Ruby": 190,
#         "proglang_rank.Kotlin": 191,
#         "proglang_rank.Swift": 192,
#         "proglang_rank.Objective-C": 193,
#         "proglang_rank.Scala": 194,
#         "proglang_rank.Go": 195,
#         "proglang_rank.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 196,
#         "proglang_rank.Rust": 197,
#         "proglang_rank.Haskell": 198,
#         "proglang_rank.HTML / CSS": 199,
#         "proglang_rank.Elixir": 200,
#         "proglang_rank.Visual Basic": 201,
#         "proglang_rank.R": 202,
#         "proglang_rank.TypeScript": 203,
#         "proglang_rank.Dart": 204,
#         "proglang_rank.Clojure / ClojureScript": 205,
#         "proglang_rank.Delphi": 206,
#         "proglang_rank.Groovy": 207,
#         "proglang_rank.Perl": 208,
#         "proglang_rank.Assembly": 209,
#         "proglang_rank.Matlab": 210,
#         "proglang_rank.Lua": 211,
#         "proglang_rank.Shell scripting languages(bash/shell/powershell)": 212,
#         "proglang_rank.Julia": 213,
#         "proglang_rank.F#": 214,
#         "proglang_rank.Other": 215
#     },
#     "tools_ci": {
#         "tools_ci.Jenkins / Hudson": 305,
#         "tools_ci.TeamCity": 306,
#         "tools_ci.Bamboo": 307,
#         "tools_ci.Microsoft Team Foundation Build": 308,
#         "tools_ci.Travis CI": 309,
#         "tools_ci.Codeship": 310,
#         "tools_ci.CircleCI": 311,
#         "tools_ci.CruiseControl": 312,
#         "tools_ci.GoCD": 313,
#         "tools_ci.Gitlab CI": 314,
#         "tools_ci.AppVeyor": 315,
#         "tools_ci.Drone": 316,
#         "tools_ci.Semaphore CI": 317,
#         "tools_ci.GitHub Actions": 318,
#         "tools_ci.Azure DevOps (former Microsoft TFS / Visual Studio Team Services)": 319,
#         "tools_ci.AWS CodePipeline / AWS CodeStar": 320,
#         "tools_ci.Google Cloud Build": 321,
#         "tools_ci.Bitbucket Pipelines": 322,
#         "tools_ci.Custom tool": 323,
#         "tools_ci.Other": 324
#     },
#     "tools_it": {
#         "tools_it.Jira": 325,
#         "tools_it.YouTrack": 326,
#         "tools_it.Redmine": 327,
#         "tools_it.GitLab Issue Board": 328,
#         "tools_it.Asana": 329,
#         "tools_it.Wrike": 330,
#         "tools_it.Microsoft TFS / Visual Studio Team Services": 331,
#         "tools_it.Trello": 332,
#         "tools_it.GitHub Issues": 333,
#         "tools_it.Other": 334
#     },
#     "tools_vcs": {
#         "tools_vcs.None": 362,
#         "tools_vcs.Concurrent Versions System (CVS)": 363,
#         "tools_vcs.Apache Subversion (SVN)": 364,
#         "tools_vcs.Git": 365,
#         "tools_vcs.Mercurial": 366,
#         "tools_vcs.Perforce": 367,
#         "tools_vcs.Plastic SCM": 368,
#         "tools_vcs.Visual Studio Team Services (VSTS)": 369,
#         "tools_vcs.Microsoft TFS": 370,
#         "tools_vcs.Other": 371
#     },
#     "contribute_os": {
#         "contribute_os": 1754
#     },
#     "hours_code_job": {
#         "hours_code_job": 1752
#     },
#     "tools_adopted": {
#         "tools_adopted.Source code collaboration tool (e_g_ GitHub, GitLab, Bitbucket)": 407,
#         "tools_adopted.Issue tracker (e_g_ Jira, YouTrack)": 408,
#         "tools_adopted.Team collaboration / task management / project / workflow management tools": 409,
#         "tools_adopted.Code review tool (e_g_ Crucible, Upsource)": 410,
#         "tools_adopted.Continuous Integration (CI) or Continuous Delivery (CD) tool (e_g_ Jenkins, TeamCity)": 411,
#         "tools_adopted.Service desk / helpdesk automation solutions (Zendesk)": 412,
#         "tools_adopted.None": 413,
#         "tools_adopted.Static analysis tool (e_g_ CodeClimate)": 414,
#         "tools_adopted.Standalone IDE (e_g_\u00a0 Visual Studio, Eclipse, IntelliJ IDEA)": 415,
#         "tools_adopted.Desktop Editor (e_g_ Sublime Text, Atom, VS Code, Vim)": 416,
#         "tools_adopted.In-cloud Editor or IDE": 417
#     },
#     "unittests_how": {
#         "unittests_how": 222
#     },
#     "team_size": {
#         "team_size": 2126
#     },
#     "advocate": {
#         "advocate": 2125
#     },
#     "team_distributed": {
#         "team_distributed": 2131
#     },
#     "java_version": {
#         "java_version.Java 13": 451,
#         "java_version.Java 12": 452,
#         "java_version.Java 11": 453,
#         "java_version.Java 10": 454,
#         "java_version.Java 9": 455,
#         "java_version.Java 8": 456,
#         "java_version.Java 7": 457,
#         "java_version.Java 6": 458,
#         "java_version.Other": 459
#     },
#     "java_app_server": {
#         "java_app_server.None": 460,
#         "java_app_server.Apache Tomcat": 461,
#         "java_app_server.Jetty": 462,
#         "java_app_server.WildFly": 463,
#         "java_app_server.JBoss EAP": 464,
#         "java_app_server.WebLogic": 465,
#         "java_app_server.WebSphere": 466,
#         "java_app_server.Liberty": 467,
#         "java_app_server.GlassFish": 468,
#         "java_app_server.Payara": 469,
#         "java_app_server.Other": 470
#     },
#     "java_app_frameworks": {
#         "java_app_frameworks.None": 471,
#         "java_app_frameworks.Netty": 472,
#         "java_app_frameworks.Undertow": 473,
#         "java_app_frameworks.Vert_x": 474,
#         "java_app_frameworks.Spark Java": 475,
#         "java_app_frameworks.Spring Boot": 476,
#         "java_app_frameworks.Other": 477
#     },
#     "java_package": {
#         "java_package.As artifacts (e_g_ WAR)": 478,
#         "java_package.I use an embedded server (e_g_ JAR)": 479,
#         "java_package.I'm not sure": 480
#     },
#     "java_web_frameworks": {
#         "java_web_frameworks.None": 491,
#         "java_web_frameworks.Spring MVC": 492,
#         "java_web_frameworks.GWT": 493,
#         "java_web_frameworks.Vaadin": 494,
#         "java_web_frameworks.Play Framework": 495,
#         "java_web_frameworks.Grails 2": 496,
#         "java_web_frameworks.Grails 3": 497,
#         "java_web_frameworks.Spring Boot": 498,
#         "java_web_frameworks.JSF": 499,
#         "java_web_frameworks.Struts 1": 500,
#         "java_web_frameworks.Struts 2": 501,
#         "java_web_frameworks.Wicket": 502,
#         "java_web_frameworks.Dropwizard": 503,
#         "java_web_frameworks.Other": 504
#     },
#     "java_buildsystem": {
#         "java_buildsystem.None": 505,
#         "java_buildsystem.Maven": 506,
#         "java_buildsystem.sbt": 507,
#         "java_buildsystem.Gradle": 508,
#         "java_buildsystem.Ant": 509,
#         "java_buildsystem.Bazel": 510,
#         "java_buildsystem.Other": 511
#     },
#     "company_size": {
#         "company_size": 2069
#     },
#     "job_role": {
#         "job_role.Developer / Programmer /  Software Engineer": 1,
#         "job_role.DevOps Engineer / Infrastructure Developer": 2,
#         "job_role.DBA": 3,
#         "job_role.Architect": 4,
#         "job_role.Tester / QA Engineer": 5,
#         "job_role.Technical Support": 6,
#         "job_role.Data Analyst / Data Engineer/ Data Scientist": 7,
#         "job_role.Business Analyst": 8,
#         "job_role.Team Lead": 9,
#         "job_role.Systems Analyst": 10,
#         "job_role.Product Manager": 11,
#         "job_role.UX / UI Designer": 12,
#         "job_role.CIO / CEO / CTO": 13,
#         "job_role.Marketing Manager": 14,
#         "job_role.Developer Advocate": 15,
#         "job_role.Instructor / Teacher / Tutor": 16,
#         "job_role.Other": 17
#     },
#     "age_range": {
#         "age_range": 76
#     },
#     "adopt_proglang": {
#         "adopt_proglang.No, I'm not planning to adopt / migrate": 145,
#         "adopt_proglang.Planning to adopt / migrate to other language(s) - Write In": 146,
#         "adopt_proglang.Java": 147,
#         "adopt_proglang.C": 148,
#         "adopt_proglang.C++": 149,
#         "adopt_proglang.Python": 150,
#         "adopt_proglang.C#": 151,
#         "adopt_proglang.PHP": 152,
#         "adopt_proglang.JavaScript": 153,
#         "adopt_proglang.Ruby": 154,
#         "adopt_proglang.Elixir": 155,
#         "adopt_proglang.Crystal": 156,
#         "adopt_proglang.Kotlin": 157,
#         "adopt_proglang.Swift": 158,
#         "adopt_proglang.Objective-C": 159,
#         "adopt_proglang.Visual Basic": 160,
#         "adopt_proglang.Scala": 161,
#         "adopt_proglang.Go": 162,
#         "adopt_proglang.HTML / CSS": 163,
#         "adopt_proglang.Haskell": 164,
#         "adopt_proglang.R": 165,
#         "adopt_proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 166,
#         "adopt_proglang.TypeScript": 167,
#         "adopt_proglang.Dart": 168,
#         "adopt_proglang.CoffeeScript": 169,
#         "adopt_proglang.Clojure / ClojureScript": 170,
#         "adopt_proglang.Delphi": 171,
#         "adopt_proglang.COBOL": 172,
#         "adopt_proglang.Groovy": 173,
#         "adopt_proglang.Rust": 174,
#         "adopt_proglang.Perl": 175,
#         "adopt_proglang.Assembly": 176,
#         "adopt_proglang.Matlab": 177,
#         "adopt_proglang.Lua": 178,
#         "adopt_proglang.Shell scripting languages(bash/shell/powershell)": 179,
#         "adopt_proglang.Julia": 180,
#         "adopt_proglang.F#": 181,
#         "adopt_proglang.Other": 182
#     },
#     "cloud_services": {
#         "cloud_services.Amazon Web Services": 1731,
#         "cloud_services.Microsoft Azure": 1732,
#         "cloud_services.Google Cloud Platform": 1733,
#         "cloud_services.Rackspace": 1734,
#         "cloud_services.RedHat OpenShift": 1735,
#         "cloud_services.IBM SoftLayer": 1736,
#         "cloud_services.Cloud Foundry": 1737,
#         "cloud_services.Heroku": 1738,
#         "cloud_services.Other": 1739
#     },
#     "tools_cloud": {
#         "tools_cloud.None": 437,
#         "tools_cloud.Continuous Integration tool": 438,
#         "tools_cloud.Continuous Delivery tool": 439,
#         "tools_cloud.Code Review tool": 440,
#         "tools_cloud.Issue Tracker": 441
#     },
#     "where_sources": {
#         "where_sources.Version control as a service (e_g_ GitHub, Bitbucket)": 442,
#         "where_sources.Manually deployed version control (e_g_ GitHub Enterprise, GitLab)": 443,
#         "where_sources.Other": 444
#     },
#     "vc_service": {
#         "vc_service.None": 372,
#         "vc_service.GitHub": 373,
#         "vc_service.GitLab": 374,
#         "vc_service.Bitbucket": 375,
#         "vc_service.Gitcolony": 376,
#         "vc_service.Perforce": 377,
#         "vc_service.Amazon CodeCommit": 378,
#         "vc_service.RhodeCode": 379,
#         "vc_service.SourceForge": 380,
#         "vc_service.Azure DevOps (former Microsoft TFS / Visual Studio Team Services)": 381,
#         "vc_service.Assembla": 382,
#         "vc_service.Helix Core Version Control": 383,
#         "vc_service.TeamForge SCM": 384,
#         "vc_service.Phabricator": 385,
#         "vc_service.Custom tool": 386,
#         "vc_service.Other": 387
#     },
#     "java_ee": {
#         "java_ee.None": 512,
#         "java_ee.Java EE 8 / Jakarta EE 8": 513,
#         "java_ee.Java EE 7": 514,
#         "java_ee.Java EE 6": 515,
#         "java_ee.Java EE 5": 516,
#         "java_ee.J2EE": 517,
#         "java_ee.Other": 518
#     },
#     "java_profiler": {
#         "java_profiler.None": 519,
#         "java_profiler.VisualVM": 520,
#         "java_profiler.JProfiler": 521,
#         "java_profiler.Java Mission Control": 522,
#         "java_profiler.YourKit": 523,
#         "java_profiler.NetBeans profiler": 524,
#         "java_profiler.Honest profiler": 525,
#         "java_profiler.async-profiler": 526,
#         "java_profiler.Own custom tools": 527,
#         "java_profiler.Other": 528
#     },
#     "java_ide": {
#         "java_ide": 529
#     },
#     "c_standart": {
#         "c_standart.C99": 549,
#         "c_standart.C11": 550,
#         "c_standart.Embedded C": 551,
#         "c_standart.Other": 552
#     },
#     "c_ide": {
#         "c_ide": 553
#     },
#     "c_unittesting": {
#         "c_unittesting.I don\u2019t write unit tests for C": 554,
#         "c_unittesting.I write unit tests, but don\u2019t use any frameworks": 555,
#         "c_unittesting.Catch": 556,
#         "c_unittesting.Google Test": 557,
#         "c_unittesting.CppUnit": 558,
#         "c_unittesting.CUnit": 559,
#         "c_unittesting.Unity": 560,
#         "c_unittesting.Other": 561
#     },
#     "c_projectmodels": {
#         "c_projectmodels.None": 562,
#         "c_projectmodels.Visual Studio project": 563,
#         "c_projectmodels.Xcode project": 564,
#         "c_projectmodels.Autotools": 565,
#         "c_projectmodels.Makefiles": 566,
#         "c_projectmodels.CMake": 567,
#         "c_projectmodels.Qmake": 568,
#         "c_projectmodels.Custom build system": 569,
#         "c_projectmodels.Other": 570
#     },
#     "c_compilers": {
#         "c_compilers.GCC": 578,
#         "c_compilers.Clang": 579,
#         "c_compilers.MSVC": 580,
#         "c_compilers.Intel": 581,
#         "c_compilers.Compiler for microcontrollers (like Keil, C51 C Compiler, IAR, etc_)": 582,
#         "c_compilers.Custom": 583,
#         "c_compilers.Other": 584
#     },
#     "cpp_standart": {
#         "cpp_standart.C++98 / C++03": 601,
#         "cpp_standart.C++11": 602,
#         "cpp_standart.C++14": 603,
#         "cpp_standart.C++17": 604,
#         "cpp_standart.C++20": 605
#     },
#     "cpp_ide": {
#         "cpp_ide": 611
#     },
#     "cpp_unittesting": {
#         "cpp_unittesting.I don\u2019t write unit tests for C++": 612,
#         "cpp_unittesting.I write unit tests, but don\u2019t use any frameworks": 613,
#         "cpp_unittesting.Boost_Test": 614,
#         "cpp_unittesting.Google Test": 615,
#         "cpp_unittesting.CppUnit": 616,
#         "cpp_unittesting.Catch": 617,
#         "cpp_unittesting.doctest": 618,
#         "cpp_unittesting.Other": 619
#     },
#     "cpp_projectmodels": {
#         "cpp_projectmodels.None": 631,
#         "cpp_projectmodels.Visual Studio project": 632,
#         "cpp_projectmodels.Xcode project": 633,
#         "cpp_projectmodels.Autotools": 634,
#         "cpp_projectmodels.Makefiles": 635,
#         "cpp_projectmodels.CMake": 636,
#         "cpp_projectmodels.Qmake": 637,
#         "cpp_projectmodels.SCons": 638,
#         "cpp_projectmodels.Boost_Build": 639,
#         "cpp_projectmodels.Bazel": 640,
#         "cpp_projectmodels.Custom build system": 641,
#         "cpp_projectmodels.Other": 642
#     },
#     "cpp_compilers": {
#         "cpp_compilers.GCC": 643,
#         "cpp_compilers.Clang": 644,
#         "cpp_compilers.MSVC": 645,
#         "cpp_compilers.Intel": 646,
#         "cpp_compilers.Custom": 647,
#         "cpp_compilers.Other": 648
#     },
#     "cpp_cli": {
#         "cpp_cli": 610
#     },
#     "cpp_project_size": {
#         "cpp_project_size": 695
#     },
#     "python_vesion": {
#         "python_vesion": 696
#     },
#     "python_ide": {
#         "python_ide": 758
#     },
#     "csharp_version": {
#         "csharp_version.C# 5 (async / await, caller info attributes)": 759,
#         "csharp_version.C# 6 (? and nameof operators, static imports, exception filters, Roslyn)": 760,
#         "csharp_version.C# 7 (pattern matching, local functions, ref locals and returns, out variables)": 761,
#         "csharp_version. C# 8 (static local functions, nullable reference types, default interface methods)": 762,
#         "csharp_version.An earlier version": 763,
#         "csharp_version.I'm not sure": 764
#     },
#     "csharp_runtimes": {
#         "csharp_runtimes._NET Framework": 765,
#         "csharp_runtimes.Mono": 766,
#         "csharp_runtimes._NET Core": 767
#     },
#     "csharp_frameworks": {
#         "csharp_frameworks.None": 768,
#         "csharp_frameworks.SharePoint": 769,
#         "csharp_frameworks.ASP_NET MVC": 770,
#         "csharp_frameworks.ASP_NET Web Forms": 771,
#         "csharp_frameworks.ASP_NET Core": 772,
#         "csharp_frameworks.Windows Presentation Foundation (WPF)": 773,
#         "csharp_frameworks.Windows Forms": 774,
#         "csharp_frameworks.Windows Communication Foundation (WCF)": 775,
#         "csharp_frameworks.Entity Framework": 776,
#         "csharp_frameworks.Unity3d": 777,
#         "csharp_frameworks.Xamarin": 778,
#         "csharp_frameworks.UWP": 779,
#         "csharp_frameworks.Azure": 780,
#         "csharp_frameworks.Other": 781
#     },
#     "csharp_ide": {
#         "csharp_ide": 782
#     },
#     "csharp_vsversion": {
#         "csharp_vsversion": 806
#     },
#     "csharp_unittesting": {
#         "csharp_unittesting.I don\u2019t write unit tests for C#": 808,
#         "csharp_unittesting.I write unit tests, but don\u2019t use any frameworks": 809,
#         "csharp_unittesting.MSTest/Visual Studio Unit Testing Framework": 810,
#         "csharp_unittesting.MSTest V2": 811,
#         "csharp_unittesting.NUnit": 812,
#         "csharp_unittesting.xUnit": 813,
#         "csharp_unittesting.Other": 814
#     },
#     "csharp_performance": {
#         "csharp_performance.None": 815,
#         "csharp_performance.YourKit Profiler": 816,
#         "csharp_performance.PerfView": 817,
#         "csharp_performance.Intel VTune Amplifier": 818,
#         "csharp_performance.SciTech _NET memory profiler": 819,
#         "csharp_performance.Windows Performance Toolkit": 820,
#         "csharp_performance.Visual Studio's built-in performance and diagnostic tools": 821,
#         "csharp_performance.dotTrace": 822,
#         "csharp_performance.dotMemory": 823,
#         "csharp_performance.ANTS Profiler": 824,
#         "csharp_performance.Other": 825
#     },
#     "php_version": {
#         "php_version.PHP 7_4": 831,
#         "php_version.PHP 7_3": 832,
#         "php_version.PHP 7_2": 833,
#         "php_version.PHP 7_1": 834,
#         "php_version.PHP 7_0": 835,
#         "php_version.PHP 5_6": 836,
#         "php_version.PHP 5_5 or older": 837,
#         "php_version.Other": 838
#     },
#     "php_devenviron": {
#         "php_devenviron.Local": 839,
#         "php_devenviron.Remote (SFTP, SSH, Remote desktop, etc_)": 840,
#         "php_devenviron.Virtualized  (Vagrant, Otto, etc_)": 841,
#         "php_devenviron.Containerized (Docker, Rocket)": 842,
#         "php_devenviron.Other": 843
#     },
#     "php_ide": {
#         "php_ide": 869
#     },
#     "php_testing": {
#         "php_testing.I don\u2019t write tests for PHP": 870,
#         "php_testing.I write tests, but don\u2019t use any frameworks": 871,
#         "php_testing.PHPUnit": 872,
#         "php_testing.Behat": 873,
#         "php_testing.PHPSpec": 874,
#         "php_testing.Codeception": 875,
#         "php_testing.SimpleTest": 876,
#         "php_testing.Infection": 877,
#         "php_testing.Other": 878
#     },
#     "js_frameworks": {
#         "js_frameworks.None": 1197,
#         "js_frameworks.AngularJS": 1198,
#         "js_frameworks.Angular": 1199,
#         "js_frameworks.React": 1200,
#         "js_frameworks.React Native": 1201,
#         "js_frameworks.Cordova / PhoneGap": 1202,
#         "js_frameworks.Express": 1203,
#         "js_frameworks.Vue_js": 1204,
#         "js_frameworks.Meteor": 1205,
#         "js_frameworks.Ember": 1206,
#         "js_frameworks.Backbone": 1207,
#         "js_frameworks.Polymer": 1208,
#         "js_frameworks.Electron": 1209,
#         "js_frameworks.Svelte": 1210,
#         "js_frameworks.Other": 1211
#     },
#     "js_ide": {
#         "js_ide": 1212
#     },
#     "js_unittesting": {
#         "js_unittesting.I don\u2019t write unit tests for JavaScript": 1213,
#         "js_unittesting.I write unit tests, but don\u2019t use any frameworks": 1214,
#         "js_unittesting.Mocha": 1215,
#         "js_unittesting.Jest": 1216,
#         "js_unittesting.Ava": 1217,
#         "js_unittesting.Karma": 1218,
#         "js_unittesting.Jasmine": 1219,
#         "js_unittesting.Other": 1220
#     },
#     "js_moduleloader": {
#         "js_moduleloader.None": 1221,
#         "js_moduleloader.Browserify": 1222,
#         "js_moduleloader.Webpack": 1223,
#         "js_moduleloader.RequireJS": 1224,
#         "js_moduleloader.SystemJS": 1225,
#         "js_moduleloader.Rollup": 1226,
#         "js_moduleloader.Parcel": 1227,
#         "js_moduleloader.Other": 1228
#     },
#     "ruby_version": {
#         "ruby_version.Ruby 2_7 preview": 1021,
#         "ruby_version.Ruby 2_6": 1022,
#         "ruby_version.Ruby 2_5": 1023,
#         "ruby_version.Ruby 2_4": 1024,
#         "ruby_version.Ruby 2_3": 1025,
#         "ruby_version.Ruby 2_2": 1026,
#         "ruby_version.Ruby 2_1 and older": 1027,
#         "ruby_version.Other": 1029,
#         "ruby_version_management.None": 1030,
#         "ruby_version_management.RVM": 1031,
#         "ruby_version_management.Rbenv": 1032,
#         "ruby_version_management.Asdf": 1033,
#         "ruby_version_management.Chruby": 1034,
#         "ruby_version_management.Docker": 1035,
#         "ruby_version_management.Other": 1036
#     },
#     "ruby_gemmanagement": {
#         "ruby_gemmanagement.None": 1037,
#         "ruby_gemmanagement.Bundler": 1038,
#         "ruby_gemmanagement.RVM gemsets": 1039,
#         "ruby_gemmanagement.Rbenv gemsets": 1040,
#         "ruby_gemmanagement.Other": 1041
#     },
#     "ruby_gems_count": {
#         "ruby_gems_count": 1042
#     },
#     "ruby_frameworks": {
#         "ruby_frameworks.None": 1043,
#         "ruby_frameworks.Ruby on Rails": 1044,
#         "ruby_frameworks.Rack": 1045,
#         "ruby_frameworks.Sinatra": 1046,
#         "ruby_frameworks.Hanami": 1047,
#         "ruby_frameworks.Grape": 1048,
#         "ruby_frameworks.Other": 1049
#     },
#     "ruby_rails_version": {
#         "ruby_rails_version": 1050,
#         "ruby_rails_version_migrate": 1051
#     },
#     "ruby_servers": {
#         "ruby_servers.None": 1052,
#         "ruby_servers.Unicorn": 1053,
#         "ruby_servers.Puma": 1054,
#         "ruby_servers.Passenger": 1055,
#         "ruby_servers.Thin": 1056,
#         "ruby_servers.Other": 1057
#     },
#     "ruby_ide": {
#         "ruby_ide": 1058
#     },
#     "ruby_unittesting": {
#         "ruby_unittesting.I don\u2019t write unit tests for Ruby": 1059,
#         "ruby_unittesting.Shoulda": 1060,
#         "ruby_unittesting.RSpec": 1061,
#         "ruby_unittesting.Cucumber": 1062,
#         "ruby_unittesting.MiniTest": 1063,
#         "ruby_unittesting.TestUnit": 1064,
#         "ruby_unittesting.Other": 1065
#     },
#     "swiftoc_unittesting": {
#         "swiftoc_unittesting.I don\u2019t write unit tests for Swift or Objective-C development": 1080,
#         "swiftoc_unittesting.I write unit tests, but don\u2019t use any frameworks": 1081,
#         "swiftoc_unittesting.XCTest": 1082,
#         "swiftoc_unittesting.Quick + Nimble": 1083,
#         "swiftoc_unittesting.Kiwi": 1084,
#         "swiftoc_unittesting.Other": 1085
#     },
#     "swiftoc_ui_tests": {
#         "swiftoc_ui_tests": 1093
#     },
#     "swiftoc_dependecymanager": {
#         "swiftoc_dependecymanager.None": 1100,
#         "swiftoc_dependecymanager.CocoaPods": 1101,
#         "swiftoc_dependecymanager.Carthage": 1102,
#         "swiftoc_dependecymanager.Swift Package Manager": 1103,
#         "swiftoc_dependecymanager.Other": 1104
#     },
#     "swiftoc_db_engine": {
#         "swiftoc_db_engine.None": 1106,
#         "swiftoc_db_engine.SQLite with my own wrapper": 1107,
#         "swiftoc_db_engine.CoreData": 1108,
#         "swiftoc_db_engine.Realm": 1109,
#         "swiftoc_db_engine.Firebase": 1110,
#         "swiftoc_db_engine.Other": 1111
#     },
#     "swiftoc_build": {
#         "swiftoc_build.I build my project from the IDE": 1114,
#         "swiftoc_build.I use Fastlane": 1115,
#         "swiftoc_build.I build on CI": 1116,
#         "swiftoc_build.Other": 1117
#     },
#     "swiftoc_linux": {
#         "swiftoc_linux": 1118
#     },
#     "sql_tool": {
#         "sql_tool.None": 1447,
#         "sql_tool.MySQL Workbench": 1448,
#         "sql_tool.pgAdmin": 1449,
#         "sql_tool.Oracle SQL Developer": 1450,
#         "sql_tool.SQL Server Management Studio": 1451,
#         "sql_tool.DataGrip": 1452,
#         "sql_tool.phpMyAdmin": 1453,
#         "sql_tool.Navicat": 1454,
#         "sql_tool.Toad": 1455,
#         "sql_tool.EMS SQL Manager": 1456,
#         "sql_tool.dbForge Studio": 1457,
#         "sql_tool.HeidiSQL": 1458,
#         "sql_tool.DbVisualizer": 1459,
#         "sql_tool.DBeaver": 1460,
#         "sql_tool.Sequel Pro": 1461,
#         "sql_tool.SQuirreL SQL": 1462,
#         "sql_tool.Command Line": 1463,
#         "sql_tool.JetBrains IDE(s) (IntelliJ IDEA, PhpStorm, etc_) with the Database plugin": 1464,
#         "sql_tool.Robo 3T": 1465,
#         "sql_tool.PL / SQL Developer": 1466,
#         "sql_tool.Other": 1467
#     },
#     "use_static_analysis": {
#         "use_static_analysis": 1751
#     },
#     "regularly_tools": {
#         "regularly_tools.Source code collaboration tool (e_g_ GitHub, GitLab, Bitbucket)": 261,
#         "regularly_tools.Issue tracker (e_g_ Jira, YouTrack)": 262,
#         "regularly_tools.Team collaboration / task management / project / workflow management tools": 263,
#         "regularly_tools.Code review tool (e_g_ Crucible, Upsource)": 264,
#         "regularly_tools.Continuous Integration (CI) or Continuous Delivery (CD) tool (e_g_ Jenkins, TeamCity)": 265,
#         "regularly_tools.Service desk / helpdesk automation solutions (Zendesk)": 266,
#         "regularly_tools.Static analysis tool (e_g_ CodeClimate)": 267,
#         "regularly_tools.Standalone IDE (e_g_\u00a0 Visual Studio, Eclipse, IntelliJ IDEA)": 268,
#         "regularly_tools.Desktop Editor (e_g_ Sublime Text, Atom, VS Code, Vim)": 269,
#         "regularly_tools.In-cloud Editor or IDE": 270,
#         "regularly_tools.None": 271
#     },
#     "visit_meetups": {
#         "visit_meetups": 2222
#     },
#     "ruby_rails_version_migrate": {
#         "ruby_rails_version_migrate": 1051
#     },
#     "scala_java_version": {
#         "scala_java_version.Java 11": 1130,
#         "scala_java_version.Java 10": 1131,
#         "scala_java_version.Java 9": 1132,
#         "scala_java_version.Java 8": 1133,
#         "scala_java_version.Other": 1134
#     },
#     "scala_frameworks_web": {
#         "scala_frameworks_web.None": 1142,
#         "scala_frameworks_web.Akka-http": 1143,
#         "scala_frameworks_web.Netty": 1144,
#         "scala_frameworks_web.Spark Java": 1145,
#         "scala_frameworks_web.Play": 1146,
#         "scala_frameworks_web.Spray": 1147,
#         "scala_frameworks_web.Spring": 1148,
#         "scala_frameworks_web.sttp": 1149,
#         "scala_frameworks_web.Http4s": 1150,
#         "scala_frameworks_web.Other": 1151
#     },
#     "scala_ide": {
#         "scala_ide": 1165,
#         "scala_ide_additional": 1166
#     },
#     "scala_buildsystem": {
#         "scala_buildsystem.Maven": 1167,
#         "scala_buildsystem.Gradle": 1168,
#         "scala_buildsystem.sbt": 1169,
#         "scala_buildsystem.Bloop": 1170,
#         "scala_buildsystem.Other": 1171
#     },
#     "scala_macros": {
#         "scala_macros": 1187
#     },
#     "target_os": {
#         "target_os.Windows": 71,
#         "target_os.Linux": 72,
#         "target_os.macOS": 73,
#         "target_os.Other": 74
#     },
#     "php_frameworks": {
#         "php_frameworks.None": 845,
#         "php_frameworks.Symfony": 846,
#         "php_frameworks.Drupal": 847,
#         "php_frameworks.WordPress": 848,
#         "php_frameworks.Zend": 849,
#         "php_frameworks.Magento": 850,
#         "php_frameworks.Laravel": 851,
#         "php_frameworks.Joomla!": 852,
#         "php_frameworks.Yii": 853,
#         "php_frameworks.CakePHP": 854,
#         "php_frameworks.CodeIgniter": 855,
#         "php_frameworks.Slim": 856,
#         "php_frameworks.Other": 857
#     },
#     "devops_conf_management": {
#         "devops_conf_management.None": 1666,
#         "devops_conf_management.Puppet": 1667,
#         "devops_conf_management.Chef": 1668,
#         "devops_conf_management.Ansible": 1669,
#         "devops_conf_management.Salt": 1670,
#         "devops_conf_management.Custom solution": 1671,
#         "devops_conf_management.Other": 1672
#     },
#     "ruby_version_management": {
#         "ruby_version_management.None": 1030,
#         "ruby_version_management.RVM": 1031,
#         "ruby_version_management.Rbenv": 1032,
#         "ruby_version_management.Asdf": 1033,
#         "ruby_version_management.Chruby": 1034,
#         "ruby_version_management.Docker": 1035,
#         "ruby_version_management.Other": 1036
#     },
#     "agile_framework": {
#         "agile_framework": 2127
#     },
#     "hours_code_hobby": {
#         "hours_code_hobby": 1753
#     },
#     "ides": {
#         "ides.RStudio": 272,
#         "ides.IntelliJ IDEA": 273,
#         "ides.Android Studio": 274,
#         "ides.Visual Studio": 275,
#         "ides.Xcode": 276,
#         "ides.PhpStorm": 277,
#         "ides.WebStorm": 278,
#         "ides.RubyMine": 279,
#         "ides.PyCharm": 280,
#         "ides.Vim": 281,
#         "ides.Sublime Text": 282,
#         "ides.Atom": 283,
#         "ides.VS Code (Visual Studio Code)": 284,
#         "ides.Notepad++": 285,
#         "ides.AppCode": 286,
#         "ides.CLion": 287,
#         "ides.Eclipse": 288,
#         "ides.NetBeans": 289,
#         "ides.QtCreator": 290,
#         "ides.Emacs": 291,
#         "ides.JetBrains Rider": 292,
#         "ides.Gedit": 293,
#         "ides.IPython/Jupyter Notebook": 294,
#         "ides.DataGrip": 295,
#         "ides.GoLand": 296,
#         "ides.Other": 297
#     },
#     "mobile_os_how": {
#         "mobile_os_how.I use native tools (Swift / Objective-C for iOS, Kotlin / Android, etc_)": 1478,
#         "mobile_os_how.I use cross-platform technologies / frameworks (Xamarin, Apache Cordova, Ionic, etc_)": 1479
#     },
#     "mobile_crossplatform_frmwrk": {
#         "mobile_crossplatform_frmwrk.Apache Flex": 1480,
#         "mobile_crossplatform_frmwrk.Corona": 1481,
#         "mobile_crossplatform_frmwrk.Ionic": 1482,
#         "mobile_crossplatform_frmwrk.Kivy": 1483,
#         "mobile_crossplatform_frmwrk.Kendo UI": 1484,
#         "mobile_crossplatform_frmwrk.Xamarin": 1485,
#         "mobile_crossplatform_frmwrk.Cordova": 1486,
#         "mobile_crossplatform_frmwrk.Unity": 1487,
#         "mobile_crossplatform_frmwrk.React Native": 1488,
#         "mobile_crossplatform_frmwrk.Flutter": 1489,
#         "mobile_crossplatform_frmwrk.PhoneGap": 1490,
#         "mobile_crossplatform_frmwrk.NativeScript": 1491,
#         "mobile_crossplatform_frmwrk.Kotlin Multiplatform": 1492,
#         "mobile_crossplatform_frmwrk.Other": 1493
#     },
#     "python_for": {
#         "python_for.Educational purposes": 697,
#         "python_for.Data analysis": 698,
#         "python_for.System administration / Writing automation scripts / Infrastructure configuration (DevOps)": 699,
#         "python_for.Software testing / writing automated tests": 700,
#         "python_for.Software prototyping": 701,
#         "python_for.Web development": 702,
#         "python_for.Programming of web parsers / scrapers / crawlers": 703,
#         "python_for.Machine learning": 704,
#         "python_for.Network programming": 705,
#         "python_for.Desktop development": 706,
#         "python_for.Computer graphics": 707,
#         "python_for.Game development": 708,
#         "python_for.Mobile development": 709,
#         "python_for.Embedded development": 710,
#         "python_for.Other": 711
#     },
#     "csharp_os": {
#         "csharp_os.Windows": 790,
#         "csharp_os.Unix / Linux": 791,
#         "csharp_os.macOS": 792,
#         "csharp_os.Other": 793
#     },
#     "csharp_vsc_plugins": {
#         "csharp_vsc_plugins.None": 794,
#         "csharp_vsc_plugins.C# for Visual Studio Code (powered by OmniSharp)": 795,
#         "csharp_vsc_plugins.NuGet Package Manager": 796,
#         "csharp_vsc_plugins.C# FixFormat": 797,
#         "csharp_vsc_plugins.C# Extensions": 798,
#         "csharp_vsc_plugins.C# XML Documentation Comments": 799,
#         "csharp_vsc_plugins.Code Runner": 800,
#         "csharp_vsc_plugins.ESLint": 801,
#         "csharp_vsc_plugins.TSLint": 802,
#         "csharp_vsc_plugins.ASP_NET Helper": 803,
#         "csharp_vsc_plugins.C# snippets": 804,
#         "csharp_vsc_plugins.Other": 805
#     },
#     "csharp_msdn": {
#         "csharp_msdn": 826,
#         "csharp_msdn_type": 827
#     },
#     "csharp_tfs": {
#         "csharp_tfs.No": 828,
#         "csharp_tfs.TFS": 829,
#         "csharp_tfs.VSTS": 830
#     },
#     "scala_version": {
#         "scala_version.2_13": 1125,
#         "scala_version.2_12": 1126,
#         "scala_version.2_11": 1127
#     },
#     "scala_compilationtarget": {
#         "scala_compilationtarget.JVM": 1128,
#         "scala_compilationtarget.scala_js": 1129
#     },
#     "scala_unittesting": {
#         "scala_unittesting.I don\u2019t write unit tests for Scala": 1135,
#         "scala_unittesting.ScalaTest": 1136,
#         "scala_unittesting.ScalaMock": 1137,
#         "scala_unittesting.JUnit": 1138,
#         "scala_unittesting.ScalaCheck": 1139,
#         "scala_unittesting.specs2": 1140,
#         "scala_unittesting.Other": 1141
#     },
#     "proglang_rank": {
#         "proglang_rank.Java": 183,
#         "proglang_rank.C": 184,
#         "proglang_rank.C++": 185,
#         "proglang_rank.Python": 186,
#         "proglang_rank.C#": 187,
#         "proglang_rank.PHP": 188,
#         "proglang_rank.JavaScript": 189,
#         "proglang_rank.Ruby": 190,
#         "proglang_rank.Kotlin": 191,
#         "proglang_rank.Swift": 192,
#         "proglang_rank.Objective-C": 193,
#         "proglang_rank.Scala": 194,
#         "proglang_rank.Go": 195,
#         "proglang_rank.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 196,
#         "proglang_rank.Rust": 197,
#         "proglang_rank.Haskell": 198,
#         "proglang_rank.HTML / CSS": 199,
#         "proglang_rank.Elixir": 200,
#         "proglang_rank.Visual Basic": 201,
#         "proglang_rank.R": 202,
#         "proglang_rank.TypeScript": 203,
#         "proglang_rank.Dart": 204,
#         "proglang_rank.Clojure / ClojureScript": 205,
#         "proglang_rank.Delphi": 206,
#         "proglang_rank.Groovy": 207,
#         "proglang_rank.Perl": 208,
#         "proglang_rank.Assembly": 209,
#         "proglang_rank.Matlab": 210,
#         "proglang_rank.Lua": 211,
#         "proglang_rank.Shell scripting languages(bash/shell/powershell)": 212,
#         "proglang_rank.Julia": 213,
#         "proglang_rank.F#": 214,
#         "proglang_rank.Other": 215
#     },
#     "python_other_techs": {
#         "python_other_techs.None": 753,
#         "python_other_techs.Sphinx": 754,
#         "python_other_techs.Buildout": 755,
#         "python_other_techs.ORM": 756,
#         "python_other_techs.Other": 757
#     },
#     "kotlin_how_long": {
#         "kotlin_how_long": 1000
#     },
#     "scala_frameworks": {
#         "scala_frameworks_web.None": 1142,
#         "scala_frameworks_web.Akka-http": 1143,
#         "scala_frameworks_web.Netty": 1144,
#         "scala_frameworks_web.Spark Java": 1145,
#         "scala_frameworks_web.Play": 1146,
#         "scala_frameworks_web.Spray": 1147,
#         "scala_frameworks_web.Spring": 1148,
#         "scala_frameworks_web.sttp": 1149,
#         "scala_frameworks_web.Http4s": 1150,
#         "scala_frameworks_web.Other": 1151,
#         "scala_frameworks.None": 1152,
#         "scala_frameworks.Twitter Util": 1153,
#         "scala_frameworks.Akka": 1154,
#         "scala_frameworks.Spark": 1155,
#         "scala_frameworks.Scalaz": 1156,
#         "scala_frameworks.Shapeless": 1157,
#         "scala_frameworks.Finagle": 1158,
#         "scala_frameworks.Cats": 1159,
#         "scala_frameworks.Slick": 1160,
#         "scala_frameworks.FS2": 1161,
#         "scala_frameworks.Monix": 1162,
#         "scala_frameworks.ZIO": 1163,
#         "scala_frameworks.Other": 1164
#     },
#     "scala_sbt": {
#         "scala_sbt.1_0": 1172,
#         "scala_sbt.0_13 or older": 1275
#     },
#     "scala_interactive": {
#         "scala_interactive.None": 1173,
#         "scala_interactive.Scala REPL": 1174,
#         "scala_interactive.sbt console": 1175,
#         "scala_interactive.Ammonite REPL": 1176,
#         "scala_interactive.Scastie": 1177,
#         "scala_interactive.IntelliJ IDEA Worksheet": 1178,
#         "scala_interactive.Scala IDE Worksheet": 1179,
#         "scala_interactive.Apache Zeppelin Notebook": 1180,
#         "scala_interactive.Jupyter Notebook": 1181,
#         "scala_interactive.Other": 1182
#     },
#     "scala_compiler_plugins": {
#         "scala_compiler_plugins.None": 1183,
#         "scala_compiler_plugins.Scalamacros/Scalameta Paradise": 1184,
#         "scala_compiler_plugins.Kind Projector": 1185,
#         "scala_compiler_plugins.Other": 1186
#     },
#     "go_multipleversions": {
#         "go_multipleversions": 1321
#     },
#     "go_gopath": {
#         "go_gopath": 1322
#     },
#     "go_multipleprojects": {
#         "go_multipleprojects": 1323
#     },
#     "go_packagemanager": {
#         "go_packagemanager.None": 1330,
#         "go_packagemanager.dep": 1331,
#         "go_packagemanager.godep": 1332,
#         "go_packagemanager.glide": 1333,
#         "go_packagemanager.govendor": 1334,
#         "go_packagemanager.Go Modules": 1335,
#         "go_packagemanager.gom": 1336,
#         "go_packagemanager.gpm": 1337,
#         "go_packagemanager.Other": 1338,
#         "go_packagemanager_migrate.No, I don't plan to": 1357,
#         "go_packagemanager_migrate.Go Modules": 1358
#     },
#     "go_packagemanager_migrate": {
#         "go_packagemanager_migrate.No, I don't plan to": 1357,
#         "go_packagemanager_migrate.Go Modules": 1358
#     },
#     "go_frameworks": {
#         "go_frameworks.None": 1359,
#         "go_frameworks.Buffalo": 1360,
#         "go_frameworks.Gin": 1361,
#         "go_frameworks.Echo": 1362,
#         "go_frameworks.Beego": 1363,
#         "go_frameworks.Revel": 1364,
#         "go_frameworks.Other": 1365
#     },
#     "go_router": {
#         "go_router.None": 1366,
#         "go_router.Standard library": 1367,
#         "go_router.gorilla / mux": 1368,
#         "go_router.go-chi / chi": 1369,
#         "go_router.julienschmidt / httproute": 1370,
#         "go_router.gocraft / web": 1371,
#         "go_router.Other": 1372
#     },
#     "go_testing": {
#         "go_testing.I don\u2019t write unit tests for Go": 1373,
#         "go_testing.I write unit tests, but don\u2019t use any frameworks": 1374,
#         "go_testing.built-in testing": 1375,
#         "go_testing.gocheck": 1376,
#         "go_testing.testify": 1377,
#         "go_testing.ginkgo": 1378,
#         "go_testing.gomega": 1379,
#         "go_testing.goconvey": 1380,
#         "go_testing.gomock": 1381,
#         "go_testing.go-sqlmock": 1382,
#         "go_testing.Other": 1383
#     },
#     "go_external_deps": {
#         "go_external_deps": 1384
#     },
#     "go_code_size": {
#         "go_code_size": 1385
#     },
#     "primary_proglang": {
#         "primary_proglang.Java": 112,
#         "primary_proglang.C": 113,
#         "primary_proglang.C++": 114,
#         "primary_proglang.Python": 115,
#         "primary_proglang.C#": 116,
#         "primary_proglang.PHP": 117,
#         "primary_proglang.JavaScript": 118,
#         "primary_proglang.Ruby": 119,
#         "primary_proglang.Kotlin": 120,
#         "primary_proglang.Swift": 121,
#         "primary_proglang.Objective-C": 122,
#         "primary_proglang.Scala": 123,
#         "primary_proglang.Go": 124,
#         "primary_proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 125,
#         "primary_proglang.Rust": 126,
#         "primary_proglang.Haskell": 127,
#         "primary_proglang.HTML / CSS": 128,
#         "primary_proglang.Elixir": 129,
#         "primary_proglang.Visual Basic": 130,
#         "primary_proglang.R": 131,
#         "primary_proglang.TypeScript": 132,
#         "primary_proglang.Dart": 133,
#         "primary_proglang.Clojure / ClojureScript": 134,
#         "primary_proglang.Delphi": 135,
#         "primary_proglang.Groovy": 136,
#         "primary_proglang.Perl": 137,
#         "primary_proglang.Assembly": 138,
#         "primary_proglang.Matlab": 139,
#         "primary_proglang.Lua": 140,
#         "primary_proglang.Shell scripting languages(bash/shell/powershell)": 141,
#         "primary_proglang.Julia": 142,
#         "primary_proglang.F#": 143,
#         "primary_proglang.Other": 144
#     },
#     "kotlin_languages_before": {
#         "kotlin_languages_before.Java": 1008,
#         "kotlin_languages_before.JavaScript/TypeScript": 1009,
#         "kotlin_languages_before.C/C++": 1010,
#         "kotlin_languages_before.C#": 1011,
#         "kotlin_languages_before.PHP": 1012,
#         "kotlin_languages_before.Ruby": 1013,
#         "kotlin_languages_before.Scala": 1014,
#         "kotlin_languages_before.Go": 1015,
#         "kotlin_languages_before.Groovy": 1016,
#         "kotlin_languages_before.Python": 1017,
#         "kotlin_languages_before.Swift": 1018,
#         "kotlin_languages_before.Other": 1019
#     },
#     "scala_ide_additional": {
#         "scala_ide_additional": 1166
#     },
#     "devops_server_templating": {
#         "devops_server_templating.None": 1673,
#         "devops_server_templating.Docker": 1674,
#         "devops_server_templating.Vagrant": 1675,
#         "devops_server_templating.Packer": 1676,
#         "devops_server_templating.CoreOS rkt": 1677,
#         "devops_server_templating.Other": 1678
#     },
#     "devops_container_orchestration": {
#         "devops_container_orchestration.None": 1690,
#         "devops_container_orchestration.Amazon ECS / Fargate": 1691,
#         "devops_container_orchestration.Amazon EKS": 1692,
#         "devops_container_orchestration.Mesos or DC / OS": 1693,
#         "devops_container_orchestration.Kubernetes (self-managed or fully managed)": 1694,
#         "devops_container_orchestration.Hashicorp Nomad": 1695,
#         "devops_container_orchestration.Docker Swarm": 1696,
#         "devops_container_orchestration.CoreOS Tectonic": 1697,
#         "devops_container_orchestration.Other": 1698
#     },
#     "devops_deploy_docker_repo": {
#         "devops_deploy_docker_repo.I do not deploy": 1703,
#         "devops_deploy_docker_repo.I use only the command line": 1704,
#         "devops_deploy_docker_repo.I use a configuration management tool (Chef, Puppet, Ansible, etc_)": 1705,
#         "devops_deploy_docker_repo.I deploy from CI / CD": 1706,
#         "devops_deploy_docker_repo.I deploy with custom / in-house tools": 1707,
#         "devops_deploy_docker_repo.Other": 1708
#     },
#     "devops_keep_artifacts": {
#         "devops_keep_artifacts.I don't keep artifacts": 1709,
#         "devops_keep_artifacts.Pulp": 1710,
#         "devops_keep_artifacts.Amazon S3": 1711,
#         "devops_keep_artifacts.Archiva": 1712,
#         "devops_keep_artifacts.NuGet": 1713,
#         "devops_keep_artifacts.Nexus": 1714,
#         "devops_keep_artifacts.JFrog Artifactory": 1715,
#         "devops_keep_artifacts.MyGet": 1716,
#         "devops_keep_artifacts.npm": 1717,
#         "devops_keep_artifacts.Docker Hub (private or public)": 1718,
#         "devops_keep_artifacts.Custom tool": 1719,
#         "devops_keep_artifacts.Other": 1720
#     },
#     "accounts": {
#         "accounts.None of the above": 2206,
#         "accounts.Facebook": 2207,
#         "accounts.Twitter": 2208,
#         "accounts.LinkedIn": 2209,
#         "accounts.QQ": 2210,
#         "accounts.Qzone": 2211,
#         "accounts.Baidu Tieba": 2212,
#         "accounts.Quora": 2213,
#         "accounts.Zhihu (\u77e5\u4e4e)": 2214,
#         "accounts.XING": 2215,
#         "accounts.Instagram": 2216,
#         "accounts.VKontakte": 2217,
#         "accounts.GitHub": 2218,
#         "accounts.Stack Overflow": 2219,
#         "accounts.Reddit": 2220,
#         "accounts.Other": 2221
#     },
#     "learn_pl": {
#         "learn_pl.I am not learning any programming languages": 1981,
#         "learn_pl.Java": 1982,
#         "learn_pl.\u0421": 1983,
#         "learn_pl.C++": 1984,
#         "learn_pl.Python": 1985,
#         "learn_pl.C#": 1986,
#         "learn_pl.PHP": 1987,
#         "learn_pl.JavaScript": 1988,
#         "learn_pl.Ruby": 1989,
#         "learn_pl.Kotlin": 1990,
#         "learn_pl.Swift": 1991,
#         "learn_pl.Scala": 1992,
#         "learn_pl.Go": 1993,
#         "learn_pl.R": 1994,
#         "learn_pl.TypeScript": 1995,
#         "learn_pl.Haskell": 1996,
#         "learn_pl.Elixir": 1997,
#         "learn_pl.Clojure": 1998,
#         "learn_pl.Rust": 1999,
#         "learn_pl.Other": 2000
#     },
#     "learn_what": {
#         "learn_what.I have not tried to learn anything new in the last 12 months": 2001,
#         "learn_what.Offline educational organizations": 2002,
#         "learn_what.Books": 2003,
#         "learn_what.Personal teacher / consultant": 2004,
#         "learn_what.Online coding schools": 2005,
#         "learn_what.MOOCs (Coursera, edX, Udacity, etc_)": 2006,
#         "learn_what.Blogs / forums": 2007,
#         "learn_what.Documentation & APIs": 2008,
#         "learn_what.Other": 2009
#     },
#     "it_core": {
#         "it_core": 2070
#     },
#     "sectors_it": {
#         "sectors_it.Telecom": 2071,
#         "sectors_it.Game Development (including mobile games)": 2072,
#         "sectors_it.Mobile Development": 2073,
#         "sectors_it.IoT / Embedded": 2074,
#         "sectors_it.IT Services": 2075,
#         "sectors_it.Cloud Computing / Platform": 2076,
#         "sectors_it.Big Data / Data Analysis": 2077,
#         "sectors_it.Hardware": 2078,
#         "sectors_it.Data center Services": 2079,
#         "sectors_it.Software Development Tools": 2080,
#         "sectors_it.Internet / Search Engines": 2081,
#         "sectors_it.Semiconductors": 2082,
#         "sectors_it.E-learning": 2083,
#         "sectors_it.Fintech": 2084,
#         "sectors_it.Healthcare IT": 2085,
#         "sectors_it.Cybersecurity": 2086,
#         "sectors_it.BPO Services": 2087,
#         "sectors_it.Other Software (all other types of software)": 2088,
#         "sectors_it.Other": 2089
#     },
#     "sectors_nonit": {
#         "sectors_nonit.Government and Defense": 2090,
#         "sectors_nonit.Administration / Management / Business Development": 2091,
#         "sectors_nonit.Banking / Real Estate / Mortgage Financing / Accounting / Finance / Insurance": 2092,
#         "sectors_nonit.Business / Strategic Management": 2093,
#         "sectors_nonit.Construction / Architecture": 2094,
#         "sectors_nonit.Customer Support": 2095,
#         "sectors_nonit.Design": 2096,
#         "sectors_nonit.Education / Training": 2097,
#         "sectors_nonit.Human Resources": 2098,
#         "sectors_nonit.Law": 2099,
#         "sectors_nonit.Logistics/ Transportation": 2100,
#         "sectors_nonit.Machinery": 2101,
#         "sectors_nonit.Aerospace": 2102,
#         "sectors_nonit.Automotive and Boating": 2103,
#         "sectors_nonit.Manufacturing": 2104,
#         "sectors_nonit.Marketing": 2105,
#         "sectors_nonit.Medicine / Health": 2106,
#         "sectors_nonit.Non-profit": 2107,
#         "sectors_nonit.Entertainment / Mass Media and Information / Publishing": 2108,
#         "sectors_nonit.Restaurants / Hospitality / Tourism": 2109,
#         "sectors_nonit.Sales / Distribution / Retail": 2110,
#         "sectors_nonit.Food / Agriculture": 2111,
#         "sectors_nonit.Science": 2112,
#         "sectors_nonit.Security": 2113,
#         "sectors_nonit.Service / Maintenance": 2114,
#         "sectors_nonit.Energy": 2115,
#         "sectors_nonit.Other": 2116
#     },
#     "pairprog_do": {
#         "pairprog_do.Yes, remote pair programming": 2128,
#         "pairprog_do.Yes, face-to-face pair programming": 2129,
#         "pairprog_do.No": 2130
#     },
#     "devops_infr_provisioning": {
#         "devops_infr_provisioning.None": 1679,
#         "devops_infr_provisioning.Terraform": 1680,
#         "devops_infr_provisioning.AWS CloudFormation": 1681,
#         "devops_infr_provisioning.AWS CDK": 1682,
#         "devops_infr_provisioning.TOSCA/Cloudify": 1683,
#         "devops_infr_provisioning.OpenStack Heat": 1684,
#         "devops_infr_provisioning.Other": 1685
#     },
#     "devops_involved": {
#         "devops_involved": 1665
#     },
#     "devops_deploy_cloud": {
#         "devops_deploy_cloud.Run scripts on your local workstation / VM": 1726,
#         "devops_deploy_cloud.Use Continuous Integration / Continuous Delivery": 1727,
#         "devops_deploy_cloud.Use your cloud provider's web interface": 1728,
#         "devops_deploy_cloud.Other": 1729
#     },
#     "kind_of_dev": {
#         "kind_of_dev.Product development": 2117,
#         "kind_of_dev.Outsourcing": 2118,
#         "kind_of_dev.Custom-tailored software / websites / applications": 2119,
#         "kind_of_dev.In-house development": 2120,
#         "kind_of_dev.Internal deployment and maintenance of third-party tools": 2121,
#         "kind_of_dev.Customer services development (websites, mobile apps, etc_)": 2122,
#         "kind_of_dev.Open source projects": 2123,
#         "kind_of_dev.Other": 2124
#     },
#     "java_unittesting": {
#         "java_unittesting.I don\u2019t write unit tests for Java": 481,
#         "java_unittesting.I write unit tests, but don\u2019t use any frameworks": 482,
#         "java_unittesting.JUnit": 483,
#         "java_unittesting.TestNG": 484,
#         "java_unittesting.Mockito": 485,
#         "java_unittesting.PowerMock": 486,
#         "java_unittesting.Spock": 487,
#         "java_unittesting.EasyMock": 488,
#         "java_unittesting.JMockit": 489,
#         "java_unittesting.Other": 490
#     },
#     "tools_use": {
#         "tools_use.Team collaboration / task management / project / workflow management tools.Free": 418,
#         "tools_use.Team collaboration / task management / project / workflow management tools.Paid": 419,
#         "tools_use.Team collaboration / task management / project / workflow management tools.Not sure": 420,
#         "tools_use.In-cloud Editor or IDE.Not sure": 421,
#         "tools_use.Service desk / helpdesk automation solutions (Zendesk).Not sure": 422,
#         "tools_use.Service desk / helpdesk automation solutions (Zendesk).Paid": 423,
#         "tools_use.In-cloud Editor or IDE.Free": 424,
#         "tools_use.Service desk / helpdesk automation solutions (Zendesk).Free": 425,
#         "tools_use.In-cloud Editor or IDE.Paid": 426
#     },
#     "swiftoc_platforms": {
#         "swiftoc_platforms.iOS": 1072,
#         "swiftoc_platforms.tvOS": 1073,
#         "swiftoc_platforms.watchOS": 1074,
#         "swiftoc_platforms.macOS": 1075,
#         "swiftoc_platforms.I don\u2019t develop for Apple platforms": 1076
#     },
#     "swiftoc_cpp_libs": {
#         "swiftoc_cpp_libs": 1079
#     },
#     "swiftoc_ui_frameworks": {
#         "swiftoc_ui_frameworks.None": 1094,
#         "swiftoc_ui_frameworks.XCTest": 1095,
#         "swiftoc_ui_frameworks.KIF": 1096,
#         "swiftoc_ui_frameworks.EarlGrey": 1097,
#         "swiftoc_ui_frameworks.iOSSnapshotTestCase (FBSnapshotTestCase)": 1098,
#         "swiftoc_ui_frameworks.Other": 1099
#     },
#     "swiftoc_db_viewer_do": {
#         "swiftoc_db_viewer_do": 1112
#     },
#     "swiftoc_together": {
#         "swiftoc_together": 1078
#     },
#     "employment_status": {
#         "employment_status": 0
#     },
#     "test_types": {
#         "test_types.None": 216,
#         "test_types.Unit": 217,
#         "test_types.Integration": 218,
#         "test_types.End-to-End": 219,
#         "test_types.Performance ": 220,
#         "test_types.Other": 221
#     },
#     "db": {
#         "db.None": 223,
#         "db.DB2": 224,
#         "db.MS SQL Server": 225,
#         "db.MySQL": 226,
#         "db.Oracle Database": 227,
#         "db.PostgreSQL": 228,
#         "db.SQLite": 229,
#         "db.Cassandra": 230,
#         "db.Couchbase": 231,
#         "db.HBase": 232,
#         "db.MongoDB": 233,
#         "db.Neo4j": 234,
#         "db.Redis": 235,
#         "db.Amazon Redshift": 236,
#         "db.H2": 237,
#         "db.MariaDB": 238,
#         "db.Exasol": 239,
#         "db.ClickHouse": 240,
#         "db.Other": 241,
#         "db_adopt.No, I'm not planning to adopt / migrate to any": 242,
#         "db_adopt.Yes, I'm planning to adopt / migrate to other database(s) - Write In": 243,
#         "db_adopt.DB2": 244,
#         "db_adopt.MS SQL Server": 245,
#         "db_adopt.MySQL": 246,
#         "db_adopt.Oracle Database": 247,
#         "db_adopt.PostgreSQL": 248,
#         "db_adopt.SQLite": 249,
#         "db_adopt.Cassandra": 250,
#         "db_adopt.Couchbase": 251,
#         "db_adopt.HBase": 252,
#         "db_adopt.MongoDB": 253,
#         "db_adopt.Neo4j": 254,
#         "db_adopt.Redis": 255,
#         "db_adopt.Amazon Redshift": 256,
#         "db_adopt.H2": 257,
#         "db_adopt.MariaDB": 258,
#         "db_adopt.ClickHouse": 259,
#         "db_adopt.Other": 260,
#         "db_how_long": 1468,
#         "db_debug_stored_proc": 1469,
#         "db_have_tests": 1470,
#         "db_keep_scripts_vcs": 1471,
#         "db_connections": 1472,
#         "db_do_comm": 1473,
#         "db_n_rows": 1474
#     },
#     "c_dependencymanager": {
#         "c_dependencymanager.None": 571,
#         "c_dependencymanager.build2": 572,
#         "c_dependencymanager.Conan": 573,
#         "c_dependencymanager.Nuget": 574,
#         "c_dependencymanager.vcpkg": 575,
#         "c_dependencymanager.I rely on a system package manager": 576,
#         "c_dependencymanager.Other": 577
#     },
#     "cpp_dependencymanager": {
#         "cpp_dependencymanager.None": 620,
#         "cpp_dependencymanager.build2": 621,
#         "cpp_dependencymanager.Conan": 622,
#         "cpp_dependencymanager.Hunter": 623,
#         "cpp_dependencymanager.Nuget": 624,
#         "cpp_dependencymanager.vcpkg": 625,
#         "cpp_dependencymanager.I rely on a system package manager": 626,
#         "cpp_dependencymanager.Other": 627
#     },
#     "cpp_guidelines_tools": {
#         "cpp_guidelines_tools.None": 668,
#         "cpp_guidelines_tools.Clang-analyzer / Clang Static Analyzer": 669,
#         "cpp_guidelines_tools.Clang-tidy": 670,
#         "cpp_guidelines_tools.Cppcheck": 671,
#         "cpp_guidelines_tools.Coverity": 672,
#         "cpp_guidelines_tools.Cpplint": 673,
#         "cpp_guidelines_tools.PVS-Studio": 674,
#         "cpp_guidelines_tools.Klocwork": 675,
#         "cpp_guidelines_tools.PC-lint / Flexelint": 676,
#         "cpp_guidelines_tools.Parasoft C/C++test": 677,
#         "cpp_guidelines_tools.Stack": 678,
#         "cpp_guidelines_tools.Tool provided by my IDE (Visual Studio, ReSharper C++, CLion, etc_)": 679,
#         "cpp_guidelines_tools.Other": 680
#     },
#     "cpp_guidelines_sources": {
#         "cpp_guidelines_sources.None": 681,
#         "cpp_guidelines_sources.Effective C++ series (books by Scott Meyers)": 682,
#         "cpp_guidelines_sources.C++ Core Guidelines \u2013 main project (github_com/isocpp/CppCoreGuidelines)": 683,
#         "cpp_guidelines_sources.Guru of the Week / Exceptional C++ series (blog/books by Herb Sutter)": 684,
#         "cpp_guidelines_sources.C++ Coding Standards (book by Herb Sutter and Andrei Alexandrescu)": 685,
#         "cpp_guidelines_sources.Abseil tips of the week": 686,
#         "cpp_guidelines_sources.Google C++ Style Guide": 687,
#         "cpp_guidelines_sources.CERT C++ Secure Coding Standard (www_securecoding_cert_org)": 688,
#         "cpp_guidelines_sources.JSF++, Joint Strike Fighter Air Vehicle": 689,
#         "cpp_guidelines_sources.Coding Standards (Lockheed Martin)": 690,
#         "cpp_guidelines_sources.High Integrity C++ Coding Standard (Programming Research)": 691,
#         "cpp_guidelines_sources.C++ Core Guidelines \u2013 a company-specific fork/branch augmented with internal rules": 692,
#         "cpp_guidelines_sources.MISRA C++ (MIRA Ltd_)": 693,
#         "cpp_guidelines_sources.Other": 694
#     },
#     "python_ds_libs": {
#         "python_ds_libs.None": 723,
#         "python_ds_libs.NumPy": 724,
#         "python_ds_libs.SciPy": 725,
#         "python_ds_libs.Pandas": 726,
#         "python_ds_libs.MXNet": 727,
#         "python_ds_libs.Matplotlib": 728,
#         "python_ds_libs.Seaborn": 729,
#         "python_ds_libs.SciKit-Learn": 730,
#         "python_ds_libs.Keras": 731,
#         "python_ds_libs.TensorFlow": 732,
#         "python_ds_libs.PyTorch": 733,
#         "python_ds_libs.Theano": 734,
#         "python_ds_libs.NLTK": 735,
#         "python_ds_libs.Gensim": 736,
#         "python_ds_libs.Other": 737
#     },
#     "python_other_libs": {
#         "python_other_libs.None": 738,
#         "python_other_libs.Requests": 739,
#         "python_other_libs.aiohttp": 740,
#         "python_other_libs.PyQT": 741,
#         "python_other_libs.PyGTK": 742,
#         "python_other_libs.wxPython": 743,
#         "python_other_libs.Pillow": 744,
#         "python_other_libs.Tkinter": 745,
#         "python_other_libs.Pygame": 746,
#         "python_other_libs.Twisted": 747,
#         "python_other_libs.Asyncio": 748,
#         "python_other_libs.Kivy": 749,
#         "python_other_libs.Six": 750,
#         "python_other_libs.Scrapy": 751,
#         "python_other_libs.Other": 752
#     },
#     "python_web_libs": {
#         "python_web_libs.None": 712,
#         "python_web_libs.Django": 713,
#         "python_web_libs.web2py": 714,
#         "python_web_libs.Bottle": 715,
#         "python_web_libs.CherryPy\u00a0": 716,
#         "python_web_libs.Flask\u00a0": 717,
#         "python_web_libs.Hug": 718,
#         "python_web_libs.Pyramid\u00a0": 719,
#         "python_web_libs.Tornado": 720,
#         "python_web_libs.Falcon": 721,
#         "python_web_libs.Other": 722
#     },
#     "js_sslang": {
#         "js_sslang.CSS": 1229,
#         "js_sslang.Sass": 1230,
#         "js_sslang.SCSS": 1231,
#         "js_sslang.Less": 1232,
#         "js_sslang.PostCSS": 1233,
#         "js_sslang.CSS-in-JS": 1234,
#         "js_sslang.CSS Modules": 1235,
#         "js_sslang.Stylus": 1236,
#         "js_sslang.Other": 1237
#     },
#     "js_graphql": {
#         "js_graphql": 1238
#     },
#     "js_monorepo": {
#         "js_monorepo": 1239
#     },
#     "learn_time": {
#         "learn_time": 2029
#     },
#     "learn_kind_of_content": {
#         "learn_kind_of_content": 2028
#     },
#     "php_qualitytools": {
#         "php_qualitytools.None": 879,
#         "php_qualitytools.Php Inspections \u200b(EA Extended)": 880,
#         "php_qualitytools.PHP_CodeSniffer": 881,
#         "php_qualitytools.PHP CS Fixer": 882,
#         "php_qualitytools.PHPMD": 883,
#         "php_qualitytools.PHPStan": 884,
#         "php_qualitytools.Psalm": 885,
#         "php_qualitytools.Phan": 886,
#         "php_qualitytools.PHP Insights": 887,
#         "php_qualitytools.Other": 888
#     },
#     "php_templateengines": {
#         "php_templateengines.None, I use pure PHP": 889,
#         "php_templateengines.None, I don\u2019t render HTML": 890,
#         "php_templateengines.Twig": 891,
#         "php_templateengines.Blade": 892,
#         "php_templateengines.Smarty": 893,
#         "php_templateengines.Mustache": 894,
#         "php_templateengines.Latte": 895,
#         "php_templateengines.Other": 896
#     },
#     "php_profiler": {
#         "php_profiler.None": 897,
#         "php_profiler.In code timers (Manual timestamps, PHPBench, Toolbars, etc_)": 898,
#         "php_profiler.Xdebug Profiler": 899,
#         "php_profiler.XHProf": 900,
#         "php_profiler.Blackfire_io": 901,
#         "php_profiler.Application performance monitoring (New Relic, Tideways, etc_)": 902,
#         "php_profiler.HTTP load testing (ab, siege, etc_)": 903,
#         "php_profiler.Other": 904
#     },
#     "devops_use_docker": {
#         "devops_use_docker.Run dockerized utilities": 1686,
#         "devops_use_docker.Run your application in one container, and backing services (e_g_ database)": 1687,
#         "devops_use_docker.Run multiple application containers (e_g_ microservices)": 1688,
#         "devops_use_docker.Other": 1689
#     },
#     "go_modules_outside": {
#         "go_modules_outside": 1386
#     },
#     "go_migrate": {
#         "go_migrate": 1387
#     },
#     "csharp_vsplugins": {
#         "csharp_vsplugins.None": 783,
#         "csharp_vsplugins.ReSharper": 784,
#         "csharp_vsplugins.ReSharper C++": 785,
#         "csharp_vsplugins.CodeRush": 786,
#         "csharp_vsplugins.Visual Assist": 787,
#         "csharp_vsplugins.Roslynator": 788,
#         "csharp_vsplugins.Other": 789
#     },
#     "csharp_vsedition": {
#         "csharp_vsedition": 807
#     },
#     "csharp_msdn_type": {
#         "csharp_msdn_type": 827
#     },
#     "swiftoc_mock": {
#         "swiftoc_mock.None": 1086,
#         "swiftoc_mock.OCMock": 1087,
#         "swiftoc_mock.OCMockito": 1088,
#         "swiftoc_mock.Expecta": 1089,
#         "swiftoc_mock.Cuckoo": 1090,
#         "swiftoc_mock.SwiftHamcrest": 1091,
#         "swiftoc_mock.Other": 1092
#     },
#     "kotlin_target": {
#         "kotlin_target.JVM": 924,
#         "kotlin_target.Android": 925,
#         "kotlin_target.Kotlin for JavaScript": 926,
#         "kotlin_target.Native": 927
#     },
#     "kotlin_jdk": {
#         "kotlin_jdk.JDK 6": 928,
#         "kotlin_jdk.JDK 7": 929,
#         "kotlin_jdk.JDK 8": 930,
#         "kotlin_jdk.JDK 9": 931,
#         "kotlin_jdk.JDK 10": 932,
#         "kotlin_jdk.JDK 11": 933,
#         "kotlin_jdk.I don't know": 934
#     },
#     "kotlin_android": {
#         "kotlin_android.4_1 \u2013 4_3_1 \u00a0Jelly Bean": 935,
#         "kotlin_android.4_4 \u2013 4_4_4 \u00a0KitKat \u00a0": 936,
#         "kotlin_android.5_0 \u2013 5_1_1 \u00a0Lollipop": 937,
#         "kotlin_android.6_0 \u2013 6_0_1 \u00a0Marshmallow": 938,
#         "kotlin_android.7_0 \u2013 7_1_2 \u00a0Nougat": 939,
#         "kotlin_android.8_0 \u2013 8_1 \u00a0Oreo": 940,
#         "kotlin_android.9_0 Pie": 941,
#         "kotlin_android.Other": 942
#     },
#     "kotlin_platforms": {
#         "kotlin_platforms.iOS (arm32, arm64, emulator x86_64)": 945,
#         "kotlin_platforms.macOS (x86_64)": 946,
#         "kotlin_platforms.Android (arm32, arm64)": 947,
#         "kotlin_platforms.Windows (mingw x86_64)": 948,
#         "kotlin_platforms.Linux (x86_64, arm32, MIPS, MIPS little endian)": 949
#     },
#     "kotlin_purposes": {
#         "kotlin_purposes.For work": 1001,
#         "kotlin_purposes.For personal/side projects\u00a0": 1002,
#         "kotlin_purposes.I occasionally play around with Kotlin (Hobby)": 1003,
#         "kotlin_purposes.Other": 1004
#     },
#     "kotlin_projecttypes": {
#         "kotlin_projecttypes.New projects": 1005,
#         "kotlin_projecttypes.Old projects (migration)": 1006,
#         "kotlin_projecttypes.Other": 1007
#     },
#     "communication_tools": {
#         "communication_tools.Email (Microsoft Mail Server, Gmail, etc_)": 298,
#         "communication_tools.Instant messaging/video calling (Slack, Skype, Hipchat, etc_)": 299,
#         "communication_tools.Video conferencing (Google Meet, Zoom, etc_)": 300,
#         "communication_tools.Calendars (Google Calendar, etc_)": 301,
#         "communication_tools.Corporate portal (MS Sharepoint, Pingboard, etc_)": 302,
#         "communication_tools.Service desk/Help desk (Zendesk, Jira Service Desk, etc_)": 303,
#         "communication_tools.None": 304
#     },
#     "space_tools_mobile": {
#         "space_tools_mobile.None": 1756,
#         "space_tools_mobile.Email (Microsoft Mail Server, Gmail, etc_)": 1757,
#         "space_tools_mobile.Instant messaging/video calling (Slack, Skype, Hipchat, etc_)": 1758,
#         "space_tools_mobile.Video conferencing (Google Meet, Zoom, etc_)": 1759,
#         "space_tools_mobile.Calendars (Google Calendar, etc_)": 1760,
#         "space_tools_mobile.Corporate portal (MS Sharepoint, Pingboard, etc_)": 1761,
#         "space_tools_mobile.Service desk/Help desk (Zendesk, Jira Service Desk, etc_)": 1762
#     },
#     "space_mail_server": {
#         "space_mail_server": 1860
#     },
#     "space_suite": {
#         "space_suite.None": 1861,
#         "space_suite.G Suite (Gmail, Google Drive, Meet, etc_)": 1862,
#         "space_suite.Office 365 (Outlook, Microsoft Teams, SharePoint, etc)": 1863,
#         "space_suite.Zoho": 1864,
#         "space_suite.Yahoo": 1865,
#         "space_suite.ProtonMail": 1866,
#         "space_suite.Other": 1867
#     },
#     "space_email_server": {
#         "space_email_server": 1876
#     },
#     "space_chat": {
#         "space_chat.Mattermost": 1894,
#         "space_chat.Telegram": 1895,
#         "space_chat.WhatsApp": 1896,
#         "space_chat.Hipchat/Stride": 1897,
#         "space_chat.Viber": 1898,
#         "space_chat.Slack": 1899,
#         "space_chat.Rocket_Chat": 1900,
#         "space_chat.Zulip": 1901,
#         "space_chat.Skype": 1902,
#         "space_chat.Google Hangouts": 1903,
#         "space_chat.IRC": 1904,
#         "space_chat.Workplace by Facebook": 1905,
#         "space_chat.Microsoft Teams": 1906,
#         "space_chat.Quip": 1907,
#         "space_chat.Zoho Cliq": 1908,
#         "space_chat.Flock": 1909,
#         "space_chat.Custom tool": 1910,
#         "space_chat.Other": 1911
#     },
#     "space_video_calls": {
#         "space_video_calls.Slack": 1912,
#         "space_video_calls.Skype": 1913,
#         "space_video_calls.Skype for Business, Lync": 1914,
#         "space_video_calls.Microsoft Teams": 1915,
#         "space_video_calls.Google Meet": 1916,
#         "space_video_calls.Polycom": 1917,
#         "space_video_calls.Zoom": 1918,
#         "space_video_calls.Workplace by Facebook": 1919,
#         "space_video_calls.Other": 1920
#     },
#     "space_knowledge_base": {
#         "space_knowledge_base.None": 1921,
#         "space_knowledge_base.Confluence": 1922,
#         "space_knowledge_base.MediaWiki": 1923,
#         "space_knowledge_base.Crowdbase": 1924,
#         "space_knowledge_base.GitHub Wiki": 1925,
#         "space_knowledge_base.Stack Overflow for Teams": 1926,
#         "space_knowledge_base.Custom": 1927,
#         "space_knowledge_base.GitLab": 1928,
#         "space_knowledge_base.Azure DevOps": 1929,
#         "space_knowledge_base.Notion": 1930,
#         "space_knowledge_base.Wrike": 1931,
#         "space_knowledge_base.Microsoft SharePoint": 1932,
#         "space_knowledge_base.Jive": 1933,
#         "space_knowledge_base.Guru": 1934,
#         "space_knowledge_base.Nuclino": 1935,
#         "space_knowledge_base.Slite": 1936,
#         "space_knowledge_base.Other": 1937
#     },
#     "space_document_collaboration": {
#         "space_document_collaboration.None": 1956,
#         "space_document_collaboration.Office 365": 1957,
#         "space_document_collaboration.Zoho Office Suite": 1958,
#         "space_document_collaboration. Confluence": 1959,
#         "space_document_collaboration.Google Docs\u00a0": 1960,
#         "space_document_collaboration.Dropbox Paper": 1961,
#         "space_document_collaboration.Quip": 1962,
#         "space_document_collaboration.Other": 1963
#     },
#     "space_file_sharing": {
#         "space_file_sharing.None": 1948,
#         "space_file_sharing.Google Drive": 1949,
#         "space_file_sharing.Dropbox": 1950,
#         "space_file_sharing.OneCloud": 1951,
#         "space_file_sharing.Microsoft OneDrive": 1952,
#         "space_file_sharing.Sharepoint": 1953,
#         "space_file_sharing.On-premise FTP server": 1954,
#         "space_file_sharing.Other": 1955
#     },
#     "swiftoc_serverside": {
#         "swiftoc_serverside": 1119,
#         "swiftoc_serverside_frameworks.Kitura": 1120,
#         "swiftoc_serverside_frameworks.Vapor": 1121,
#         "swiftoc_serverside_frameworks.Perfect": 1122,
#         "swiftoc_serverside_frameworks.Other": 1123
#     },
#     "swiftoc_serverside_frameworks": {
#         "swiftoc_serverside_frameworks.Kitura": 1120,
#         "swiftoc_serverside_frameworks.Vapor": 1121,
#         "swiftoc_serverside_frameworks.Perfect": 1122,
#         "swiftoc_serverside_frameworks.Other": 1123
#     },
#     "rust_how": {
#         "rust_how.Work": 1240,
#         "rust_how.Personal / side projects": 1241,
#         "rust_how.Hobby": 1242,
#         "rust_how.Other": 1243,
#         "rust_how_long": 1244,
#         "rust_how_debug": 1288
#     },
#     "rust_how_long": {
#         "rust_how_long": 1244
#     },
#     "rust_other_langs": {
#         "rust_other_langs.None": 1245,
#         "rust_other_langs.C": 1246,
#         "rust_other_langs.C++": 1247,
#         "rust_other_langs.Python": 1248,
#         "rust_other_langs.Java": 1249,
#         "rust_other_langs.Go": 1250,
#         "rust_other_langs.JavaScript": 1251,
#         "rust_other_langs.PHP": 1252,
#         "rust_other_langs.Other": 1253
#     },
#     "rust_code_interact": {
#         "rust_code_interact.Language interop (foreign functions)": 1254,
#         "rust_code_interact.RPC": 1255,
#         "rust_code_interact.REST API": 1256,
#         "rust_code_interact.Other": 1257
#     },
#     "rust_ide": {
#         "rust_ide.Atom": 1266,
#         "rust_ide.Emacs": 1267,
#         "rust_ide.IntelliJ IDEA": 1268,
#         "rust_ide.CLion": 1269,
#         "rust_ide.Sublime Text": 1270,
#         "rust_ide.Vim": 1271,
#         "rust_ide.Visual Studio": 1272,
#         "rust_ide.Visual Studio Code": 1273,
#         "rust_ide.Other": 1274
#     },
#     "rust_profiler": {
#         "rust_profiler.I don\u2019t use profiling tools": 1289,
#         "rust_profiler.perf": 1290,
#         "rust_profiler.gprof": 1291,
#         "rust_profiler.callgrind/cachegrind": 1292,
#         "rust_profiler.DTrace": 1293,
#         "rust_profiler.Other": 1294
#     },
#     "ai_replace_court_trust": {
#         "ai_replace_court_trust": 1627
#     },
#     "rust_install_windows": {
#         "rust_install_windows.rustup_rs": 1258,
#         "rust_install_windows.Build from sources": 1259,
#         "rust_install_windows.Official Windows _msi installer": 1260,
#         "rust_install_windows.Linux distribution package": 1261,
#         "rust_install_windows.Official tarball": 1262,
#         "rust_install_windows.Homebrew": 1263,
#         "rust_install_windows.Official MacOS _pkg installer": 1264,
#         "rust_install_windows.Other": 1265
#     },
#     "rust_platforms": {
#         "rust_platforms.Linux": 1311,
#         "rust_platforms.Windows": 1312,
#         "rust_platforms.macOS": 1313,
#         "rust_platforms.Android": 1314,
#         "rust_platforms.iOS": 1315,
#         "rust_platforms.WebAssembly": 1316,
#         "rust_platforms.Embedded": 1317,
#         "rust_platforms.Other": 1318
#     },
#     "rust_devs_count": {
#         "rust_devs_count": 1319
#     },
#     "cats_dogs": {
#         "cats_dogs": 2030
#     },
#     "rust_primary_ide": {
#         "rust_primary_ide": 1277
#     },
#     "space_calendar": {
#         "space_calendar.Google Calendar": 1877,
#         "space_calendar.Outlook": 1878,
#         "space_calendar.iCal (Calendar App in Mac)": 1879,
#         "space_calendar.Microsoft Exchange": 1880,
#         "space_calendar.IBM Domino": 1881,
#         "space_calendar.Fantastical": 1882,
#         "space_calendar.Other": 1883
#     },
#     "space_mail_service": {
#         "space_mail_service.I don\u2019t know": 1868,
#         "space_mail_service.Gmail (as part of G Suite)": 1869,
#         "space_mail_service.Microsoft Outlook (as part of Office 365)": 1870,
#         "space_mail_service.Microsoft Exchange Server": 1871,
#         "space_mail_service.MDaemon": 1872,
#         "space_mail_service.OpenSMTPD": 1873,
#         "space_mail_service.We don\u2019t have a company email service, everyone can use different email services (Gmail, Yahoo, etc_)_": 1874,
#         "space_mail_service.Other": 1875
#     },
#     "where_host": {
#         "where_host.Locally (on your workstation, developer environment, or device)": 1722,
#         "where_host.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1723,
#         "where_host.Cloud Service (AWS, MS Azure, GCP, etc_)": 1724,
#         "where_host.Other": 1725,
#         "where_host_primarly": 1730,
#         "where_host_plan.Locally (on your workstation, developer environment or device)": 1740,
#         "where_host_plan.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1741,
#         "where_host_plan.Amazon Web Services": 1742,
#         "where_host_plan.Microsoft Azure": 1743,
#         "where_host_plan.Google Cloud Platform": 1744,
#         "where_host_plan.Rackspace": 1745,
#         "where_host_plan.RedHat OpenShift": 1746,
#         "where_host_plan.IBM SoftLayer": 1747,
#         "where_host_plan.Cloud Foundry": 1748,
#         "where_host_plan.Heroku": 1749,
#         "where_host_plan.Other": 1750
#     },
#     "where_host_primarly": {
#         "where_host_primarly": 1730
#     },
#     "where_host_plan": {
#         "where_host_plan.Locally (on your workstation, developer environment or device)": 1740,
#         "where_host_plan.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1741,
#         "where_host_plan.Amazon Web Services": 1742,
#         "where_host_plan.Microsoft Azure": 1743,
#         "where_host_plan.Google Cloud Platform": 1744,
#         "where_host_plan.Rackspace": 1745,
#         "where_host_plan.RedHat OpenShift": 1746,
#         "where_host_plan.IBM SoftLayer": 1747,
#         "where_host_plan.Cloud Foundry": 1748,
#         "where_host_plan.Heroku": 1749,
#         "where_host_plan.Other": 1750
#     },
#     "rust_projecttypes": {
#         "rust_projecttypes.Web Development": 1295,
#         "rust_projecttypes.Systems Programming": 1296,
#         "rust_projecttypes.DevOps": 1297,
#         "rust_projecttypes.Network Programming": 1298,
#         "rust_projecttypes.Databases": 1299,
#         "rust_projecttypes.Security": 1300,
#         "rust_projecttypes.Finance / Commerce": 1301,
#         "rust_projecttypes.Data Science": 1302,
#         "rust_projecttypes.Mobile": 1303,
#         "rust_projecttypes.Desktop / GUI Applications": 1304,
#         "rust_projecttypes.Embedded devices / Internet of Things": 1305,
#         "rust_projecttypes.Academic / Scientific / Numeric": 1306,
#         "rust_projecttypes.Machine Learning / Artificial Intelligence": 1307,
#         "rust_projecttypes.Blockchain": 1308,
#         "rust_projecttypes.Games": 1309,
#         "rust_projecttypes.Other": 1310
#     },
#     "go_how": {
#         "go_how": 1320
#     },
#     "kotlin_server_client": {
#         "kotlin_server_client.Server-side (like Node_js)": 943,
#         "kotlin_server_client.Browser": 944
#     },
#     "go_templateengines": {
#         "go_templateengines.None": 1324,
#         "go_templateengines.text/template": 1325,
#         "go_templateengines.html/template": 1326,
#         "go_templateengines.Plush": 1327,
#         "go_templateengines.Pongo2": 1328,
#         "go_templateengines.Other": 1329
#     },
#     "go_ide": {
#         "go_ide": 1339
#     },
#     "position_level": {
#         "position_level": 18
#     },
#     "do_crossplatform": {
#         "do_crossplatform": 1582
#     },
#     "crossplatform_platform": {
#         "crossplatform_platform.Windows": 1583,
#         "crossplatform_platform.Unix/Linux": 1584,
#         "crossplatform_platform.macOS": 1585,
#         "crossplatform_platform.iOS": 1586,
#         "crossplatform_platform.Android": 1587,
#         "crossplatform_platform.Web": 1588,
#         "crossplatform_platform.Embedded": 1589,
#         "crossplatform_platform.Other": 1590
#     },
#     "crossplatform_how_os": {
#         "crossplatform_how_os.Using containers (e_g_ Docker, Vagrant)": 1591,
#         "crossplatform_how_os.Using VMs (e_g_ VirtualBox, vSphere)": 1592,
#         "crossplatform_how_os.Using physical machines/devices": 1593,
#         "crossplatform_how_os.I don\u2019t normally work with different OS / platforms": 1594,
#         "crossplatform_how_os.Other": 1595
#     },
#     "vcs_how": {
#         "vcs_how.From the terminal": 445,
#         "vcs_how.Using specialized tools (e_g_ GitKraken, Sourcetree, GitHub desktop, etc_)": 446,
#         "vcs_how.From the IDE": 447,
#         "vcs_how.From a web browser": 448,
#         "vcs_how.Other": 449
#     },
#     "is_testing_integral": {
#         "is_testing_integral": 1510
#     },
#     "do_case_design": {
#         "do_case_design": 1511
#     },
#     "test_design_how": {
#         "test_design_how": 1512
#     },
#     "testing_types": {
#         "testing_types.None": 1513,
#         "testing_types.Regression testing": 1514,
#         "testing_types.Functional testing": 1515,
#         "testing_types.Security testing": 1516,
#         "testing_types.Usability testing": 1517,
#         "testing_types.Performance testing": 1518,
#         "testing_types.Stress testing": 1519,
#         "testing_types.Stability testing": 1520,
#         "testing_types.Smoke testing": 1521,
#         "testing_types.I\u2019m not sure": 1522,
#         "testing_types.Other": 1523
#     },
#     "testers_qa_ratio": {
#         "testers_qa_ratio": 1524
#     },
#     "store_testcases": {
#         "store_testcases.I don\u2019t use any specific tools": 1527,
#         "store_testcases.Microsoft Office documents (such as Excel spreadsheets)": 1528,
#         "store_testcases.Special test case management tools": 1529,
#         "store_testcases.Other": 1530
#     },
#     "test_management_tools": {
#         "test_management_tools.None": 1531,
#         "test_management_tools.Zephyr": 1532,
#         "test_management_tools.TestFLO for JIRA": 1533,
#         "test_management_tools.TestRail": 1534,
#         "test_management_tools.Other": 1535
#     },
#     "automated_tests": {
#         "automated_tests": 1536
#     },
#     "auto_tests_pl": {
#         "auto_tests_pl.None": 1572,
#         "auto_tests_pl.Python": 1573,
#         "auto_tests_pl.JavaScript": 1574,
#         "auto_tests_pl.Java": 1575,
#         "auto_tests_pl.Kotlin": 1576,
#         "auto_tests_pl.C#": 1577,
#         "auto_tests_pl.Perl": 1578,
#         "auto_tests_pl.Ruby": 1579,
#         "auto_tests_pl.Tcl": 1580,
#         "auto_tests_pl.Other": 1581
#     },
#     "testers_qa_pskills": {
#         "testers_qa_pskills": 1525
#     },
#     "testers_qa_manual": {
#         "testers_qa_manual": 1526
#     },
#     "auto_tests_frameworks": {
#         "auto_tests_frameworks.None": 1537,
#         "auto_tests_frameworks.TestNG": 1538,
#         "auto_tests_frameworks.JUnit": 1539,
#         "auto_tests_frameworks.NUnit / xUnit_Net": 1540,
#         "auto_tests_frameworks.MSTest / VSTest": 1541,
#         "auto_tests_frameworks.Robot Framework": 1542,
#         "auto_tests_frameworks.Serenity (Thucydides)": 1543,
#         "auto_tests_frameworks.Cucumber": 1544,
#         "auto_tests_frameworks.SpecFlow": 1545,
#         "auto_tests_frameworks.RSpec": 1546,
#         "auto_tests_frameworks.ExtentReports": 1547,
#         "auto_tests_frameworks.Selenium WebDriver": 1548,
#         "auto_tests_frameworks.Allure": 1549,
#         "auto_tests_frameworks.Other": 1550
#     },
#     "auto_tests_tools": {
#         "auto_tests_tools.None": 1551,
#         "auto_tests_tools.SoapUI": 1552,
#         "auto_tests_tools.TestComplete": 1553,
#         "auto_tests_tools.Apache JMeter": 1554,
#         "auto_tests_tools.Gauge": 1555,
#         "auto_tests_tools.HP UFT / QTP": 1556,
#         "auto_tests_tools.Katalon Studio": 1557,
#         "auto_tests_tools.FitNesse": 1558,
#         "auto_tests_tools.Rational Functional Tester": 1559,
#         "auto_tests_tools.Ranorex": 1560,
#         "auto_tests_tools.Postman": 1561,
#         "auto_tests_tools.Squish": 1562,
#         "auto_tests_tools.Other": 1563
#     },
#     "testing_platforms": {
#         "testing_platforms.None": 1564,
#         "testing_platforms.SauceLabs": 1565,
#         "testing_platforms.BrowserStack": 1566,
#         "testing_platforms.CrossBrowserTesting": 1567,
#         "testing_platforms.Kobiton": 1568,
#         "testing_platforms.Perfecto": 1569,
#         "testing_platforms.TestingBot": 1570,
#         "testing_platforms.Other": 1571
#     },
#     "go_buildsystem": {
#         "go_buildsystem.Go build": 1388,
#         "go_buildsystem.Bazel": 1389,
#         "go_buildsystem.Other": 1390
#     },
#     "devops_run_cont_apps": {
#         "devops_run_cont_apps.None": 1699,
#         "devops_run_cont_apps.Docker Compose": 1700,
#         "devops_run_cont_apps.Minikube": 1701,
#         "devops_run_cont_apps.Other": 1702
#     },
#     "kotlin_app_types": {
#         "kotlin_app_types.Web Back-end": 950,
#         "kotlin_app_types.Web Front-end": 951,
#         "kotlin_app_types.Mobile": 952,
#         "kotlin_app_types.Desktop": 953,
#         "kotlin_app_types.Data Analysis / Business Intelligence": 954,
#         "kotlin_app_types.Machine Learning": 955,
#         "kotlin_app_types.Game Development": 956,
#         "kotlin_app_types.IoT": 957,
#         "kotlin_app_types.Embedded": 958,
#         "kotlin_app_types.Library or Framework": 959,
#         "kotlin_app_types.Tooling": 960,
#         "kotlin_app_types.Other": 961
#     },
#     "lifestyle_infosource": {
#         "lifestyle_infosource.TV": 2154,
#         "lifestyle_infosource.News websites / Aggregated news sites": 2155,
#         "lifestyle_infosource.Social media": 2156,
#         "lifestyle_infosource.Community forums (Reddit, Stack Overflow)": 2157,
#         "lifestyle_infosource.Podcasts": 2158,
#         "lifestyle_infosource.Print media (magazines / newspapers)": 2159,
#         "lifestyle_infosource.Wikis": 2160,
#         "lifestyle_infosource.Radio": 2161,
#         "lifestyle_infosource.Books": 2162,
#         "lifestyle_infosource.Other websites": 2163,
#         "lifestyle_infosource.Other": 2164
#     },
#     "lifestyle_adblock": {
#         "lifestyle_adblock": 2165
#     },
#     "lifestyle_smartphone": {
#         "lifestyle_smartphone": 2166
#     },
#     "lifestyle_personal_data": {
#         "lifestyle_personal_data": 2167
#     },
#     "lifestyle_confs": {
#         "lifestyle_confs_reasons.Gain new knowledge": 2173,
#         "lifestyle_confs_reasons.Network": 2174,
#         "lifestyle_confs_reasons.Travel": 2175,
#         "lifestyle_confs_reasons.Enjoy the atmosphere": 2176,
#         "lifestyle_confs_reasons.Promote employer or yourself (for speakers)": 2177,
#         "lifestyle_confs_reasons.Other": 2178
#     },
#     "lifestyle_confs_reasons": {
#         "lifestyle_confs_reasons.Gain new knowledge": 2173,
#         "lifestyle_confs_reasons.Network": 2174,
#         "lifestyle_confs_reasons.Travel": 2175,
#         "lifestyle_confs_reasons.Enjoy the atmosphere": 2176,
#         "lifestyle_confs_reasons.Promote employer or yourself (for speakers)": 2177,
#         "lifestyle_confs_reasons.Other": 2178
#     },
#     "lifestyle_charity": {
#         "lifestyle_charity": 2179,
#         "lifestyle_charity_reasons.Provide for the basic needs of the very poor": 2180,
#         "lifestyle_charity_reasons.Give the disadvantaged a way to help themselves": 2181,
#         "lifestyle_charity_reasons.Give others some of the opportunities you\u2019ve enjoyed": 2182,
#         "lifestyle_charity_reasons.Address the fundamental problems of our world": 2183,
#         "lifestyle_charity_reasons.Provide services that governments can\u2019t or won\u2019t": 2184,
#         "lifestyle_charity_reasons.Make my community a better place to live in": 2185,
#         "lifestyle_charity_reasons.Support the positive efforts of my friends, colleagues, or family": 2186,
#         "lifestyle_charity_reasons.Make the world a better place to live in": 2187,
#         "lifestyle_charity_reasons.Make decisions on where my money goes instead of letting the government decide": 2188,
#         "lifestyle_charity_reasons.Ensure a place for diversity of cultures and beliefs": 2189,
#         "lifestyle_charity_reasons.Build ties across communities": 2190,
#         "lifestyle_charity_reasons.Other": 2191,
#         "lifestyle_charity_practices.I work for a charity organization": 2192,
#         "lifestyle_charity_practices.I volunteer what help I can (without relying on any training or professional skills)": 2193,
#         "lifestyle_charity_practices.I volunteer professional help (relying on my training or professional skills)": 2194,
#         "lifestyle_charity_practices.I donate to charity from time to time": 2195,
#         "lifestyle_charity_practices.I have recurring donations set up": 2196,
#         "lifestyle_charity_practices.Other": 2197,
#         "lifestyle_charity_imp.Fighting diseases": 2198,
#         "lifestyle_charity_imp.Fighting social inequality": 2199,
#         "lifestyle_charity_imp.Helping animals": 2200,
#         "lifestyle_charity_imp.Caring for the environment": 2201,
#         "lifestyle_charity_imp.Preventing abuse (such as family abuse)": 2202,
#         "lifestyle_charity_imp.Helping children": 2203,
#         "lifestyle_charity_imp.Helping the disadvantaged (such as the homeless)": 2204,
#         "lifestyle_charity_imp.Other": 2205
#     },
#     "lifestyle_charity_reasons": {
#         "lifestyle_charity_reasons.Provide for the basic needs of the very poor": 2180,
#         "lifestyle_charity_reasons.Give the disadvantaged a way to help themselves": 2181,
#         "lifestyle_charity_reasons.Give others some of the opportunities you\u2019ve enjoyed": 2182,
#         "lifestyle_charity_reasons.Address the fundamental problems of our world": 2183,
#         "lifestyle_charity_reasons.Provide services that governments can\u2019t or won\u2019t": 2184,
#         "lifestyle_charity_reasons.Make my community a better place to live in": 2185,
#         "lifestyle_charity_reasons.Support the positive efforts of my friends, colleagues, or family": 2186,
#         "lifestyle_charity_reasons.Make the world a better place to live in": 2187,
#         "lifestyle_charity_reasons.Make decisions on where my money goes instead of letting the government decide": 2188,
#         "lifestyle_charity_reasons.Ensure a place for diversity of cultures and beliefs": 2189,
#         "lifestyle_charity_reasons.Build ties across communities": 2190,
#         "lifestyle_charity_reasons.Other": 2191
#     },
#     "lifestyle_charity_practices": {
#         "lifestyle_charity_practices.I work for a charity organization": 2192,
#         "lifestyle_charity_practices.I volunteer what help I can (without relying on any training or professional skills)": 2193,
#         "lifestyle_charity_practices.I volunteer professional help (relying on my training or professional skills)": 2194,
#         "lifestyle_charity_practices.I donate to charity from time to time": 2195,
#         "lifestyle_charity_practices.I have recurring donations set up": 2196,
#         "lifestyle_charity_practices.Other": 2197
#     },
#     "lifestyle_charity_imp": {
#         "lifestyle_charity_imp.Fighting diseases": 2198,
#         "lifestyle_charity_imp.Fighting social inequality": 2199,
#         "lifestyle_charity_imp.Helping animals": 2200,
#         "lifestyle_charity_imp.Caring for the environment": 2201,
#         "lifestyle_charity_imp.Preventing abuse (such as family abuse)": 2202,
#         "lifestyle_charity_imp.Helping children": 2203,
#         "lifestyle_charity_imp.Helping the disadvantaged (such as the homeless)": 2204,
#         "lifestyle_charity_imp.Other": 2205
#     },
#     "lifestyle_hobbies": {
#         "lifestyle_hobbies.I have no spare time for hobbies": 388,
#         "lifestyle_hobbies.Programming": 389,
#         "lifestyle_hobbies.Sports (doing)": 390,
#         "lifestyle_hobbies.Sports (watching)": 391,
#         "lifestyle_hobbies.Video games": 392,
#         "lifestyle_hobbies.Reading": 393,
#         "lifestyle_hobbies.Watching TV": 394,
#         "lifestyle_hobbies.Spending time with family": 395,
#         "lifestyle_hobbies.Fishing / Hunting": 396,
#         "lifestyle_hobbies.Gardening": 397,
#         "lifestyle_hobbies.Listening to music": 398,
#         "lifestyle_hobbies.Traveling": 399,
#         "lifestyle_hobbies.Sleeping": 400,
#         "lifestyle_hobbies.Socializing": 401,
#         "lifestyle_hobbies.Music (playing)": 402,
#         "lifestyle_hobbies.Board games": 403,
#         "lifestyle_hobbies.Art": 404,
#         "lifestyle_hobbies.Writing": 405,
#         "lifestyle_hobbies.Other": 406
#     },
#     "lifestyle_pet": {
#         "lifestyle_pet.None": 2223,
#         "lifestyle_pet.Cat": 2224,
#         "lifestyle_pet.Dog": 2225,
#         "lifestyle_pet.Fish": 2226,
#         "lifestyle_pet.Bird": 2227,
#         "lifestyle_pet.Snake": 2228,
#         "lifestyle_pet.Insect / Spider": 2229,
#         "lifestyle_pet.Guinea pig / Hamster": 2230,
#         "lifestyle_pet.Rat / Mouse": 2231,
#         "lifestyle_pet.Other": 2232
#     },
#     "lifestyle_egift": {
#         "lifestyle_egift": 2233
#     },
#     "pull_requests": {
#         "pull_requests": 450
#     },
#     "code_yrs": {
#         "code_yrs": 75
#     },
#     "ruby_front_js": {
#         "ruby_front_js.I don\u2019t use such frameworks with Ruby on Rails_": 1066,
#         "ruby_front_js.React": 1067,
#         "ruby_front_js.Angular": 1068,
#         "ruby_front_js.AngularJS": 1069,
#         "ruby_front_js.Vue_js": 1070,
#         "ruby_front_js.Other": 1071
#     },
#     "cpp_err_report_mthds": {
#         "cpp_err_report_mthds.Exceptions (throw, try, catch)": 628,
#         "cpp_err_report_mthds.Numeric error codes (e_g_, errc, error_code, HRESULT)": 629,
#         "cpp_err_report_mthds.Success/failure result class types  (e_g_, Boost_Expected, Boost_Outcome)": 630
#     },
#     "php_how_debug": {
#         "php_how_debug": 844
#     },
#     "php_async_libs": {
#         "php_async_libs.ReactPHP": 858,
#         "php_async_libs.Amp": 859,
#         "php_async_libs.Swoole": 860,
#         "php_async_libs.I don\u2019t use any": 861,
#         "php_async_libs.Other": 862
#     },
#     "php_run_apps_prod": {
#         "php_run_apps_prod.php-fpm": 863,
#         "php_run_apps_prod.mod_php": 864,
#         "php_run_apps_prod.Other process manager (RoadRunner, php-pm, etc_)": 865,
#         "php_run_apps_prod.Serverless (AWS Lambda, Azure Functions, GCP Functions, etc_)": 866,
#         "php_run_apps_prod.I have no idea": 867,
#         "php_run_apps_prod.Other": 868
#     },
#     "php_how_evolve": {
#         "php_how_evolve": 905
#     },
#     "php_miss_ftrs": {
#         "php_miss_ftrs": 906
#     },
#     "mooc_platform": {
#         "mooc_platform.edX": 2010,
#         "mooc_platform.Coursera": 2011,
#         "mooc_platform.Khan Academy": 2012,
#         "mooc_platform.Udemy": 2013,
#         "mooc_platform.Stepik": 2014,
#         "mooc_platform.Canvas": 2015,
#         "mooc_platform.FutureLearn": 2016,
#         "mooc_platform.Udacity": 2017,
#         "mooc_platform.CodeAcademy": 2018,
#         "mooc_platform.DataCamp": 2019,
#         "mooc_platform.Egghead": 2020,
#         "mooc_platform.Pluralsight": 2021,
#         "mooc_platform.JavaRush": 2022,
#         "mooc_platform.The Open University": 2023,
#         "mooc_platform.SWAYAM": 2024,
#         "mooc_platform.Stanford Lagunita": 2025,
#         "mooc_platform.Mir\u00edadaX": 2026,
#         "mooc_platform.Other": 2027
#     },
#     "team_tools_exp": {
#         "team_tools_exp.Jira": 427,
#         "team_tools_exp.YouTrack": 428,
#         "team_tools_exp.Other": 429,
#         "team_tools_exp.Redmine": 430,
#         "team_tools_exp.GitLab Issue Board": 431,
#         "team_tools_exp.Asana": 432,
#         "team_tools_exp.Wrike": 433,
#         "team_tools_exp.Microsoft TFS / Visual Studio Team Services": 434,
#         "team_tools_exp.Trello": 435,
#         "team_tools_exp.GitHub Issues": 436
#     },
#     "team_tools_use": {
#         "team_tools_use.Confluence": 335,
#         "team_tools_use.Monday_com": 336,
#         "team_tools_use.YouTrack": 337,
#         "team_tools_use.Redmine": 338,
#         "team_tools_use.GitLab Issue Board": 339,
#         "team_tools_use.Asana": 340,
#         "team_tools_use.Wrike": 341,
#         "team_tools_use.Microsoft TFS / Visual Studio Team Services": 342,
#         "team_tools_use.Trello": 343,
#         "team_tools_use.GitHub Issues": 344,
#         "team_tools_use.GitLab": 345,
#         "team_tools_use.Azure DevOps": 346,
#         "team_tools_use.Assembla": 347,
#         "team_tools_use.Phabricator": 348,
#         "team_tools_use.Basecamp": 349,
#         "team_tools_use.Bitrix24": 350,
#         "team_tools_use.FogBugz": 351,
#         "team_tools_use.Notion": 352,
#         "team_tools_use.Jira Software": 353,
#         "team_tools_use.Jira Core": 354,
#         "team_tools_use.Jira Align": 355,
#         "team_tools_use.Targetprocess": 356,
#         "team_tools_use.Zoho Sprints": 357,
#         "team_tools_use.Rally Software (CA Agile Central)": 358,
#         "team_tools_use.Microsoft Project": 359,
#         "team_tools_use.Custom tool": 360,
#         "team_tools_use.Other": 361
#     },
#     "bigdata_platform_use": {
#         "bigdata_platform_use.No specific platform": 1636,
#         "bigdata_platform_use.Databricks": 1637,
#         "bigdata_platform_use.Cloudera Data Platform": 1638,
#         "bigdata_platform_use.Qubole": 1639,
#         "bigdata_platform_use.Zeppelin": 1640,
#         "bigdata_platform_use.Google Collab": 1641,
#         "bigdata_platform_use.Microsoft Azure HDInsight": 1642,
#         "bigdata_platform_use.Google AI Platform": 1643,
#         "bigdata_platform_use.Other": 1644
#     },
#     "bigdata_spark_version_use": {
#         "bigdata_spark_version_use.None": 1658,
#         "bigdata_spark_version_use.2_4": 1659,
#         "bigdata_spark_version_use.2_3\u00a0": 1660,
#         "bigdata_spark_version_use.2_0 - 2_2": 1661,
#         "bigdata_spark_version_use.Custom distribution of spark": 1662,
#         "bigdata_spark_version_use.Other": 1663
#     },
#     "bigdata_tools_use": {
#         "bigdata_tools_use.None": 1645,
#         "bigdata_tools_use.Apache Spark": 1646,
#         "bigdata_tools_use.Apache Kafka": 1647,
#         "bigdata_tools_use.Apache Samza": 1648,
#         "bigdata_tools_use.Apache Flink": 1649,
#         "bigdata_tools_use.Apache Hadoop/MapReduce": 1650,
#         "bigdata_tools_use.Apache Hive": 1651,
#         "bigdata_tools_use.Apache Pig": 1652,
#         "bigdata_tools_use.Apache Tez": 1653,
#         "bigdata_tools_use.Apache Beam": 1654,
#         "bigdata_tools_use.Dask": 1655,
#         "bigdata_tools_use.Jupyter": 1656,
#         "bigdata_tools_use.Other": 1657
#     },
#     "bigdata_where_hosted": {
#         "bigdata_where_hosted": 1664
#     },
#     "db_how_long": {
#         "db_how_long": 1468
#     },
#     "db_debug_stored_proc": {
#         "db_debug_stored_proc": 1469
#     },
#     "db_have_tests": {
#         "db_have_tests": 1470
#     },
#     "db_keep_scripts_vcs": {
#         "db_keep_scripts_vcs": 1471
#     },
#     "db_connections": {
#         "db_connections": 1472
#     },
#     "db_do_comm": {
#         "db_do_comm": 1473
#     },
#     "db_n_rows": {
#         "db_n_rows": 1474
#     },
#     "mcrsrvc_design_approaches": {
#         "mcrsrvc_design_approaches.None": 1597,
#         "mcrsrvc_design_approaches.Actor systems": 1598,
#         "mcrsrvc_design_approaches.CQRS": 1599,
#         "mcrsrvc_design_approaches.Monolith with web front-end": 1600,
#         "mcrsrvc_design_approaches.Microservices": 1601,
#         "mcrsrvc_design_approaches.Service-Oriented Architecture": 1602,
#         "mcrsrvc_design_approaches.Reactive streams": 1603,
#         "mcrsrvc_design_approaches.Other": 1604
#     },
#     "mcrsrvc_parts_communicate": {
#         "mcrsrvc_parts_communicate.None": 1605,
#         "mcrsrvc_parts_communicate.Cross-platform RPC (gRPC, Apache Thrift)": 1606,
#         "mcrsrvc_parts_communicate.Custom TCP/UDP communication": 1607,
#         "mcrsrvc_parts_communicate.GraphQL": 1608,
#         "mcrsrvc_parts_communicate.Message Queue": 1609,
#         "mcrsrvc_parts_communicate.Remoting (RMI, JMX)": 1610,
#         "mcrsrvc_parts_communicate.REST": 1611,
#         "mcrsrvc_parts_communicate.RPC over HTTP": 1612,
#         "mcrsrvc_parts_communicate.SOAP": 1613,
#         "mcrsrvc_parts_communicate.Stream Processing": 1614,
#         "mcrsrvc_parts_communicate.WebSocket": 1615,
#         "mcrsrvc_parts_communicate.Other": 1616
#     },
#     "mcrsrvc_code_or_spec": {
#         "mcrsrvc_code_or_spec": 1617
#     },
#     "mcrsrvc_how_declare": {
#         "mcrsrvc_how_declare.I don't document APIs": 1618,
#         "mcrsrvc_how_declare.GraphQL": 1619,
#         "mcrsrvc_how_declare.Open API (Swagger)": 1620,
#         "mcrsrvc_how_declare.RAML": 1621,
#         "mcrsrvc_how_declare.Wiki system": 1622,
#         "mcrsrvc_how_declare.WSDL": 1623,
#         "mcrsrvc_how_declare.Other": 1624
#     },
#     "mcrsrvc_store_api_spec": {
#         "mcrsrvc_store_api_spec": 1625
#     },
#     "mcrsrvc_how_vcs": {
#         "mcrsrvc_how_vcs": 1626
#     },
#     "pairprog_tools_remote": {
#         "pairprog_tools_remote.None": 2133,
#         "pairprog_tools_remote.Remote desktop": 2134,
#         "pairprog_tools_remote.Video call with screen sharing": 2135,
#         "pairprog_tools_remote.Editor / IDE with collaboration feature": 2136,
#         "pairprog_tools_remote.Other": 2137
#     },
#     "pairprog_ide": {
#         "pairprog_ide.Visual Studio Code LiveShare": 2138,
#         "pairprog_ide.Visual Studio LiveShare": 2139,
#         "pairprog_ide.Atom Teletype": 2140,
#         "pairprog_ide.SublimeText RemoteCollab": 2141,
#         "pairprog_ide.Other": 2142
#     },
#     "pairprog_how_cloud": {
#         "pairprog_how_cloud.I don't use cloud services during development": 2143,
#         "pairprog_how_cloud.I don't build applications locally, I am using remote machine in the cloud": 2144,
#         "pairprog_how_cloud.I develop applications with source code stored in the cloud": 2145,
#         "pairprog_how_cloud.I am debugging applications running in the cloud": 2146,
#         "pairprog_how_cloud.Other": 2147
#     },
#     "pairprog_why_cloud": {
#         "pairprog_why_cloud.My local machine is not powerful enough for builds / development": 2148,
#         "pairprog_why_cloud.It is hard to reproduce the application environment for local development": 2149,
#         "pairprog_why_cloud.Specific hardware is installed on the remote machine": 2150,
#         "pairprog_why_cloud.Information security reasons": 2151,
#         "pairprog_why_cloud.Data that I'm working with is stored in the cloud": 2152,
#         "pairprog_why_cloud.Other": 2153
#     },
#     "r_version": {
#         "r_version": 1391
#     },
#     "r_distrib": {
#         "r_distrib.R base (CRAN)": 1392,
#         "r_distrib.Microsoft Open R (MRAN)": 1393,
#         "r_distrib.MS SQL Server R Services": 1394,
#         "r_distrib.Oracle R Enterprise": 1395,
#         "r_distrib.I don't know": 1396,
#         "r_distrib.Other": 1397
#     },
#     "r_ide": {
#         "r_ide.RStudio": 1398,
#         "r_ide.PyCharm": 1399,
#         "r_ide.Visual Studio": 1400,
#         "r_ide.Visual Studio Code": 1401,
#         "r_ide.Jupyter Notebook": 1402,
#         "r_ide.Other": 1403
#     },
#     "r_what_for": {
#         "r_what_for.Educational purposes": 1404,
#         "r_what_for.Data analysis": 1405,
#         "r_what_for.Programming of parsers/scrapers/ETL scripts etc_": 1406,
#         "r_what_for.Machine learning": 1407,
#         "r_what_for.Other": 1408
#     },
#     "r_do_libs": {
#         "r_do_libs": 1409
#     },
#     "r_use_libs": {
#         "r_use_libs.None": 1410,
#         "r_use_libs.arules": 1411,
#         "r_use_libs.caret": 1412,
#         "r_use_libs.data_table": 1413,
#         "r_use_libs.devtools": 1414,
#         "r_use_libs.dplyr": 1415,
#         "r_use_libs.dtplyr": 1416,
#         "r_use_libs.e1071": 1417,
#         "r_use_libs.gbm": 1418,
#         "r_use_libs.ggplot2": 1419,
#         "r_use_libs.glmnet": 1420,
#         "r_use_libs.htmlwidgets": 1421,
#         "r_use_libs.igraph": 1422,
#         "r_use_libs.kernlab": 1423,
#         "r_use_libs.nnet": 1424,
#         "r_use_libs.packrat": 1425,
#         "r_use_libs.plotly": 1426,
#         "r_use_libs.randomForest": 1427,
#         "r_use_libs.RCPP": 1428,
#         "r_use_libs.rpart": 1429,
#         "r_use_libs.shiny": 1430,
#         "r_use_libs.SparkR": 1431,
#         "r_use_libs.stringi": 1432,
#         "r_use_libs.stringr": 1433,
#         "r_use_libs.XGBoost": 1434,
#         "r_use_libs.Other": 1435
#     },
#     "r_most_used_libs": {
#         "r_most_used_libs": 1436
#     },
#     "r_code_form": {
#         "r_code_form.pure _R files": 1437,
#         "r_code_form.Rmarkdown (_Rmd files)": 1438,
#         "r_code_form.shiny applications": 1439,
#         "r_code_form.R code inside some specific environment (other programming languages, databases, tools)": 1440,
#         "r_code_form.Other": 1441
#     },
#     "r_execute": {
#         "r_execute.Local machine": 1442,
#         "r_execute.Server (virtual machine)": 1443,
#         "r_execute.Cluster": 1444,
#         "r_execute.Cloud service": 1445,
#         "r_execute.Other": 1446
#     },
#     "swiftoc_plan_catalyst": {
#         "swiftoc_plan_catalyst": 1077
#     },
#     "swiftoc_plan_spm": {
#         "swiftoc_plan_spm": 1105
#     },
#     "swiftoc_ide": {
#         "swiftoc_ide": 1124
#     },
#     "edu_type_of_inst": {
#         "edu_type_of_inst": 2031
#     },
#     "edu_degree": {
#         "edu_degree": 2032
#     },
#     "edu_major_sub": {
#         "edu_major_sub": 2033
#     },
#     "devops_cryptocur": {
#         "devops_cryptocur": 1721
#     },
#     "laptop_or_desktop": {
#         "laptop_or_desktop": 1755
#     },
#     "bigdata_stat_libs": {
#         "bigdata_stat_libs.None": 1628,
#         "bigdata_stat_libs.Statistica": 1629,
#         "bigdata_stat_libs.SPSS": 1630,
#         "bigdata_stat_libs.Spreadsheet editor (Microsoft Excel, OpenOffice Calc, Google Sheets, etc_)": 1631,
#         "bigdata_stat_libs.Stata": 1632,
#         "bigdata_stat_libs.SAS": 1633,
#         "bigdata_stat_libs.Tableau": 1634,
#         "bigdata_stat_libs.Other": 1635
#     },
#     "space_use_dashboards": {
#         "space_use_dashboards": 1763
#     },
#     "rust_missed_ftrs": {
#         "rust_missed_ftrs.None": 1278,
#         "rust_missed_ftrs.Docker Support": 1279,
#         "rust_missed_ftrs.WebAssembly Debugging": 1280,
#         "rust_missed_ftrs.REPL": 1281,
#         "rust_missed_ftrs.Database Frameworks Support": 1282,
#         "rust_missed_ftrs.AWS Lambda Support": 1283,
#         "rust_missed_ftrs.Cross-language Navigation and Refactorings": 1284,
#         "rust_missed_ftrs.Embedded Development Support": 1285,
#         "rust_missed_ftrs.Remote Development Support": 1286,
#         "rust_missed_ftrs.Other": 1287
#     },
#     "work_day_start": {
#         "work_day_start": 2132
#     },
#     "rust_how_debug": {
#         "rust_how_debug": 1288
#     },
#     "edu_pl": {
#         "edu_pl.None": 2034,
#         "edu_pl.Haskell": 2035,
#         "edu_pl.Python": 2036,
#         "edu_pl.Java": 2037,
#         "edu_pl.C++": 2038,
#         "edu_pl.C#": 2039,
#         "edu_pl.C": 2040,
#         "edu_pl.PHP": 2041,
#         "edu_pl.Pascal": 2042,
#         "edu_pl.Kotlin": 2043,
#         "edu_pl.JavaScript": 2044,
#         "edu_pl.R": 2045,
#         "edu_pl.Other": 2046
#     },
#     "edu_tools_adviced": {
#         "edu_tools_adviced.RStudio": 2047,
#         "edu_tools_adviced.IntelliJ IDEA": 2048,
#         "edu_tools_adviced.Android Studio": 2049,
#         "edu_tools_adviced.Visual Studio": 2050,
#         "edu_tools_adviced.Xcode": 2051,
#         "edu_tools_adviced.PhpStorm": 2052,
#         "edu_tools_adviced.WebStorm": 2053,
#         "edu_tools_adviced.PyCharm": 2054,
#         "edu_tools_adviced.Vi / Vim": 2055,
#         "edu_tools_adviced.Sublime Text": 2056,
#         "edu_tools_adviced.Atom": 2057,
#         "edu_tools_adviced.Visual Studio Code": 2058,
#         "edu_tools_adviced.Notepad++": 2059,
#         "edu_tools_adviced.CLion": 2060,
#         "edu_tools_adviced.Eclipse": 2061,
#         "edu_tools_adviced.NetBeans": 2062,
#         "edu_tools_adviced.QtCreator": 2063,
#         "edu_tools_adviced.Emacs": 2064,
#         "edu_tools_adviced.JetBrains Rider": 2065,
#         "edu_tools_adviced.Gedit": 2066,
#         "edu_tools_adviced.IPython/Jupyter Notebook": 2067,
#         "edu_tools_adviced.Other": 2068
#     },
#     "activities_kinds": {
#         "activities_kinds.None": 23,
#         "activities_kinds.Academic Research": 24,
#         "activities_kinds.Coding / Programming": 25,
#         "activities_kinds.Code Reviewing": 26,
#         "activities_kinds.Testing": 27,
#         "activities_kinds.System Design": 28,
#         "activities_kinds.Graphics Design / Art": 29,
#         "activities_kinds.Infrastructure Development / DevOps": 30,
#         "activities_kinds.System Administration": 31,
#         "activities_kinds.Deployment": 32,
#         "activities_kinds.Business Intelligence": 33,
#         "activities_kinds.Data Analysis": 34,
#         "activities_kinds.Data Engineering": 35,
#         "activities_kinds.Machine Learning": 36,
#         "activities_kinds.Teaching Programming": 37,
#         "activities_kinds.People Management": 38,
#         "activities_kinds.Product Management": 39,
#         "activities_kinds.Technical Writing": 40,
#         "activities_kinds.UX/UI Design/Research": 41,
#         "activities_kinds.Other": 42
#     },
#     "target_platforms": {
#         "target_platforms.I don't develop anything": 43,
#         "target_platforms.Desktop": 44,
#         "target_platforms.Mobile": 45,
#         "target_platforms.Web (Back-end)": 46,
#         "target_platforms.Web (Front-end)": 47,
#         "target_platforms.Consoles (Xbox / PlayStation / Nintendo etc_)": 48,
#         "target_platforms.Server / Infrastructure": 49,
#         "target_platforms.IoT / Embedded": 50,
#         "target_platforms.WebAssembly": 51,
#         "target_platforms.Other - Write In (Required)": 52
#     },
#     "sw_types_developed": {
#         "sw_types_developed.I don\u2019t develop anything": 53,
#         "sw_types_developed.Augmented Reality / Virtual Reality": 54,
#         "sw_types_developed.Business Intelligence / Data Science / Machine Learning": 55,
#         "sw_types_developed.Blockchain": 56,
#         "sw_types_developed.Database / Data Storage": 57,
#         "sw_types_developed.Entertainment": 58,
#         "sw_types_developed.Fintech": 59,
#         "sw_types_developed.Games": 60,
#         "sw_types_developed.Hardware": 61,
#         "sw_types_developed.Home Automation": 62,
#         "sw_types_developed.IT Infrastructure": 63,
#         "sw_types_developed.Libraries / Frameworks": 64,
#         "sw_types_developed.Programming Tools": 65,
#         "sw_types_developed.Security": 66,
#         "sw_types_developed.System Software": 67,
#         "sw_types_developed.Utilities (small apps for small tasks)": 68,
#         "sw_types_developed.Websites": 69,
#         "sw_types_developed.Other": 70
#     },
#     "java_sw_developed": {
#         "java_sw_developed.None": 530,
#         "java_sw_developed.Other": 531,
#         "java_sw_developed.Augmented Reality / Virtual Reality": 532,
#         "java_sw_developed.Business Intelligence / Data Science / Machine Learning": 533,
#         "java_sw_developed.Blockchain": 534,
#         "java_sw_developed.Database / Data Storage": 535,
#         "java_sw_developed.Entertainment": 536,
#         "java_sw_developed.Fintech": 537,
#         "java_sw_developed.Games": 538,
#         "java_sw_developed.Hardware": 539,
#         "java_sw_developed.Home Automation": 540,
#         "java_sw_developed.IT Infrastructure": 541,
#         "java_sw_developed.Libraries / Frameworks": 542,
#         "java_sw_developed.Programming Tools": 543,
#         "java_sw_developed.Security": 544,
#         "java_sw_developed.System Software": 545,
#         "java_sw_developed.Utilities (small apps for small tasks)": 546,
#         "java_sw_developed.Websites": 547,
#         "java_sw_developed.Other_882": 548
#     },
#     "c_sw_developed": {
#         "c_sw_developed.None": 585,
#         "c_sw_developed.Other": 586,
#         "c_sw_developed.Business Intelligence / Data Science / Machine Learning": 587,
#         "c_sw_developed.Database / Data Storage": 588,
#         "c_sw_developed.Entertainment": 589,
#         "c_sw_developed.Fintech": 590,
#         "c_sw_developed.Games": 591,
#         "c_sw_developed.Hardware": 592,
#         "c_sw_developed.Home Automation": 593,
#         "c_sw_developed.IT Infrastructure": 594,
#         "c_sw_developed.Libraries / Frameworks": 595,
#         "c_sw_developed.Programming Tools": 596,
#         "c_sw_developed.Security": 597,
#         "c_sw_developed.System Software": 598,
#         "c_sw_developed.Utilities (small apps for small tasks)": 599,
#         "c_sw_developed.Other_884": 600
#     },
#     "cpp_sw_developed": {
#         "cpp_sw_developed.None": 649,
#         "cpp_sw_developed.Other": 650,
#         "cpp_sw_developed.Augmented Reality / Virtual Reality": 651,
#         "cpp_sw_developed.Business Intelligence / Data Science / Machine Learning": 652,
#         "cpp_sw_developed.Blockchain": 653,
#         "cpp_sw_developed.Database / Data Storage": 654,
#         "cpp_sw_developed.Entertainment": 655,
#         "cpp_sw_developed.Fintech": 656,
#         "cpp_sw_developed.Games": 657,
#         "cpp_sw_developed.Hardware": 658,
#         "cpp_sw_developed.Home Automation": 659,
#         "cpp_sw_developed.IT Infrastructure": 660,
#         "cpp_sw_developed.Libraries / Frameworks": 661,
#         "cpp_sw_developed.Programming Tools": 662,
#         "cpp_sw_developed.Security": 663,
#         "cpp_sw_developed.System Software": 664,
#         "cpp_sw_developed.Utilities (small apps for small tasks)": 665,
#         "cpp_sw_developed.Websites": 666,
#         "cpp_sw_developed.Other_886": 667
#     },
#     "mobile_ndevs_ios_andoid": {
#         "mobile_ndevs_ios_andoid": 1494
#     },
#     "mobile_apps_functionality": {
#         "mobile_apps_functionality": 1495
#     },
#     "mobile_apps_components": {
#         "mobile_apps_components.Networking": 1496,
#         "mobile_apps_components.State and Navigation Management": 1497,
#         "mobile_apps_components.Data Storage": 1498,
#         "mobile_apps_components.Security": 1499,
#         "mobile_apps_components.Computations": 1500,
#         "mobile_apps_components.Media (Image, Video, Audio)": 1501,
#         "mobile_apps_components.Payments": 1502,
#         "mobile_apps_components.ML": 1503,
#         "mobile_apps_components.File I/O": 1504,
#         "mobile_apps_components.Data Synchronization": 1505,
#         "mobile_apps_components.Other": 1506,
#         "mobile_apps_components.None of the Above": 1507
#     },
#     "mobile_UI_native_imp": {
#         "mobile_UI_native_imp": 1508
#     },
#     "mobbile_UI_perfom_imp": {
#         "mobbile_UI_perfom_imp": 1509
#     },
#     "scala_use_dotty": {
#         "scala_use_dotty": 1196
#     },
#     "scala_tools": {
#         "scala_tools.None": 1188,
#         "scala_tools.Scoverage": 1189,
#         "scala_tools.Scalafmt": 1190,
#         "scala_tools.Scalafix": 1191,
#         "scala_tools.Scapegoat": 1192,
#         "scala_tools.Scalastyle": 1193,
#         "scala_tools.Wart Remover": 1194,
#         "scala_tools.Other": 1195
#     },
#     "go_sw_peveloped": {
#         "go_sw_peveloped.None": 1340,
#         "go_sw_peveloped.Other": 1341,
#         "go_sw_peveloped.Business Intelligence / Data Science / Machine Learning": 1342,
#         "go_sw_peveloped.Blockchain": 1343,
#         "go_sw_peveloped.Database / Data Storage": 1344,
#         "go_sw_peveloped.Entertainment": 1345,
#         "go_sw_peveloped.Fintech": 1346,
#         "go_sw_peveloped.Games": 1347,
#         "go_sw_peveloped.Home Automation": 1348,
#         "go_sw_peveloped.IT Infrastructure": 1349,
#         "go_sw_peveloped.Libraries / Frameworks": 1350,
#         "go_sw_peveloped.Programming Tools": 1351,
#         "go_sw_peveloped.Security": 1352,
#         "go_sw_peveloped.System Software": 1353,
#         "go_sw_peveloped.Utilities (small apps for small tasks)": 1354,
#         "go_sw_peveloped.Websites": 1355,
#         "go_sw_peveloped.Other_895": 1356
#     },
#     "kotlin_jb_libs": {
#         "kotlin_jb_libs.None": 962,
#         "kotlin_jb_libs.I don\u2019t know": 963,
#         "kotlin_jb_libs.Kodein DI": 964,
#         "kotlin_jb_libs.kotlin-wrappers/kotlin-react": 965,
#         "kotlin_jb_libs.kotlin-wrappers/kotlin-css": 966,
#         "kotlin_jb_libs.kotlin-wrappers/*": 967,
#         "kotlin_jb_libs.kotlinx_coroutines": 968,
#         "kotlin_jb_libs.kotlinx_html": 969,
#         "kotlin_jb_libs.kotlinx_dom": 970,
#         "kotlin_jb_libs.kotlinx_serialization": 971,
#         "kotlin_jb_libs.kotlin_test": 972,
#         "kotlin_jb_libs.Ktor": 973,
#         "kotlin_jb_libs.Exposed": 974,
#         "kotlin_jb_libs.Other": 975
#     },
#     "kotlin_libs": {
#         "kotlin_libs.None": 976,
#         "kotlin_libs.I don't know": 977,
#         "kotlin_libs.KotlinTest": 978,
#         "kotlin_libs.RxKotlin": 979,
#         "kotlin_libs.TornadoFX": 980,
#         "kotlin_libs.mockito-kotlin": 981,
#         "kotlin_libs.Jackson": 982,
#         "kotlin_libs.ktlint": 983,
#         "kotlin_libs.detekt": 984,
#         "kotlin_libs.Spek": 985,
#         "kotlin_libs.Spring/Spring Boot": 986,
#         "kotlin_libs.RxBinding": 987,
#         "kotlin_libs.RxJava": 988,
#         "kotlin_libs.Okio": 989,
#         "kotlin_libs.MockK": 990,
#         "kotlin_libs.Kodein DI": 991,
#         "kotlin_libs.Arrow": 992,
#         "kotlin_libs.Gson": 993,
#         "kotlin_libs.KotlinPoet": 994,
#         "kotlin_libs.Koin": 995,
#         "kotlin_libs.MvRx": 996,
#         "kotlin_libs.Timber": 997,
#         "kotlin_libs.SQLDelight": 998,
#         "kotlin_libs.Other": 999
#     },
#     "mcrsrvc_do": {
#         "mcrsrvc_do": 1596
#     },
#     "cpp_move_11": {
#         "cpp_move_11": 607
#     },
#     "cpp_move_14": {
#         "cpp_move_14": 608
#     },
#     "cpp_move_17": {
#         "cpp_move_17": 609
#     },
#     "cpp_move_98": {
#         "cpp_move_98": 606
#     },
#     "php_sw_developed": {
#         "php_sw_developed.None": 907,
#         "php_sw_developed.Other": 908,
#         "php_sw_developed.Business Intelligence / Data Science / Machine Learning": 909,
#         "php_sw_developed.Blockchain": 910,
#         "php_sw_developed.Database / Data Storage": 911,
#         "php_sw_developed.Entertainment": 912,
#         "php_sw_developed.Fintech": 913,
#         "php_sw_developed.Games": 914,
#         "php_sw_developed.Home Automation": 915,
#         "php_sw_developed.IT Infrastructure": 916,
#         "php_sw_developed.Libraries / Frameworks": 917,
#         "php_sw_developed.Programming Tools": 918,
#         "php_sw_developed.Security": 919,
#         "php_sw_developed.System Software": 920,
#         "php_sw_developed.Utilities (small apps for small tasks)": 921,
#         "php_sw_developed.Websites": 922,
#         "php_sw_developed.Other_908": 923
#     },
#     "kotlin_ide": {
#         "kotlin_ide": 1020
#     },
#     "space_tools_blogging": {
#         "space_tools_blogging.None": 1938,
#         "space_tools_blogging.Basecamp": 1939,
#         "space_tools_blogging.Notion": 1940,
#         "space_tools_blogging.Microsoft SharePoint": 1941,
#         "space_tools_blogging.Jive": 1942,
#         "space_tools_blogging.Facebook Workplace": 1943,
#         "space_tools_blogging.Confluence": 1944,
#         "space_tools_blogging.BlogIn": 1945,
#         "space_tools_blogging.Custom tool": 1946,
#         "space_tools_blogging.Other": 1947
#     },
#     "space_tools_calendar": {
#         "space_tools_calendar.None": 1884,
#         "space_tools_calendar.Basecamp": 1885,
#         "space_tools_calendar.Igloo": 1886,
#         "space_tools_calendar.Notion": 1887,
#         "space_tools_calendar.Microsoft SharePoint": 1888,
#         "space_tools_calendar.Jive": 1889,
#         "space_tools_calendar.Facebook Workplace": 1890,
#         "space_tools_calendar.Confluence": 1891,
#         "space_tools_calendar.Custom tool": 1892,
#         "space_tools_calendar.Other": 1893
#     },
#     "space_tools_employee": {
#         "space_tools_employee.None": 1964,
#         "space_tools_employee.Bitrix24": 1965,
#         "space_tools_employee.Microsoft SharePoint": 1966,
#         "space_tools_employee.OneDirectory": 1967,
#         "space_tools_employee.Pingboard": 1968,
#         "space_tools_employee.Custom tool": 1969,
#         "space_tools_employee.Other": 1970
#     },
#     "space_tooling_stack": {
#         "space_tooling_stack.We do not have any specific stack": 1971,
#         "space_tooling_stack.Microsoft (Azure DevOps / Microsoft TFS / VSTS, Office 365)": 1972,
#         "space_tooling_stack.Atlassian (Jira, Bitbucket, Crucible, Confluence, Trello)": 1973,
#         "space_tooling_stack.Google (Cloud, G Suite, Hangouts)": 1974,
#         "space_tooling_stack.Zoho (Calendar, Sprints, Cliq)": 1975,
#         "space_tooling_stack.Amazon (AWS, CodeStar / CodeCommit / CodePipeline)": 1976,
#         "space_tooling_stack.GitHub": 1977,
#         "space_tooling_stack.GitLab": 1978,
#         "space_tooling_stack.Assembla": 1979,
#         "space_tooling_stack.Other": 1980
#     },
#     "space_tools_code_review": {
#         "space_tools_code_review.None": 1818,
#         "space_tools_code_review.GitHub": 1819,
#         "space_tools_code_review.GitLab": 1820,
#         "space_tools_code_review.Azure DevOps": 1821,
#         "space_tools_code_review.Phabricator": 1822,
#         "space_tools_code_review.Bitbucket": 1823,
#         "space_tools_code_review.Upsource": 1824,
#         "space_tools_code_review.Gerrit": 1825,
#         "space_tools_code_review.AWS CodeCommit / AWS CodeStar": 1826,
#         "space_tools_code_review.Crucible": 1827,
#         "space_tools_code_review.Collaborator": 1828,
#         "space_tools_code_review.Helix Swarm": 1829,
#         "space_tools_code_review.Review Board": 1830,
#         "space_tools_code_review.Custom tool": 1831,
#         "space_tools_code_review.Other": 1832
#     },
#     "space_tools_repo": {
#         "space_tools_repo.None": 1797,
#         "space_tools_repo.GitHub": 1798,
#         "space_tools_repo.GitLab": 1799,
#         "space_tools_repo.Azure DevOps": 1800,
#         "space_tools_repo.Assembla": 1801,
#         "space_tools_repo.Helix Core Version Control": 1802,
#         "space_tools_repo.Codefresh": 1803,
#         "space_tools_repo.JFrog Artifactory": 1804,
#         "space_tools_repo.Sonatype Nexus Repository": 1805,
#         "space_tools_repo.Docker Hub": 1806,
#         "space_tools_repo.Docker Trusted Registry": 1807,
#         "space_tools_repo.AWS Elastic Container Registry": 1808,
#         "space_tools_repo.Azure Container Registry": 1809,
#         "space_tools_repo.Google Container Registry": 1810,
#         "space_tools_repo.RedHat Quay": 1811,
#         "space_tools_repo.ProGet": 1812,
#         "space_tools_repo.Archiva": 1813,
#         "space_tools_repo.NuGet": 1814,
#         "space_tools_repo.npm": 1815,
#         "space_tools_repo.Custom tool": 1816,
#         "space_tools_repo.Other": 1817
#     },
#     "country": {
#         "country": 77
#     },
#     "space_tools_ci_2": {
#         "space_tools_ci_2.None": 1776,
#         "space_tools_ci_2.Jenkins / Hudson": 1777,
#         "space_tools_ci_2.Other": 1778,
#         "space_tools_ci_2.TeamCity": 1779,
#         "space_tools_ci_2.Bamboo": 1780,
#         "space_tools_ci_2.Microsoft Team Foundation Build": 1781,
#         "space_tools_ci_2.Travis CI": 1782,
#         "space_tools_ci_2.Codeship": 1783,
#         "space_tools_ci_2.CircleCI": 1784,
#         "space_tools_ci_2.GoCD": 1785,
#         "space_tools_ci_2.Gitlab CI": 1786,
#         "space_tools_ci_2.AppVeyor": 1787,
#         "space_tools_ci_2.Drone": 1788,
#         "space_tools_ci_2.Semaphore CI": 1789,
#         "space_tools_ci_2.GitHub Actions": 1790,
#         "space_tools_ci_2.Azure DevOps (former Microsoft TFS / Visual Studio Team Services)": 1791,
#         "space_tools_ci_2.AWS CodePipeline / AWS CodeStar": 1792,
#         "space_tools_ci_2.Google Cloud Build": 1793,
#         "space_tools_ci_2.Bitbucket Pipelines": 1794,
#         "space_tools_ci_2.Custom tool": 1795,
#         "space_tools_ci_2.Other_931": 1796
#     },
#     "space_tools_projmanag_2": {
#         "space_tools_projmanag_2.None": 1833,
#         "space_tools_projmanag_2.Confluence": 1834,
#         "space_tools_projmanag_2.Other": 1835,
#         "space_tools_projmanag_2.Monday_com": 1836,
#         "space_tools_projmanag_2.YouTrack": 1837,
#         "space_tools_projmanag_2.Redmine": 1838,
#         "space_tools_projmanag_2.GitLab Issue Board": 1839,
#         "space_tools_projmanag_2.Asana": 1840,
#         "space_tools_projmanag_2.Wrike": 1841,
#         "space_tools_projmanag_2.Microsoft TFS / Visual Studio Team Services": 1842,
#         "space_tools_projmanag_2.Trello": 1843,
#         "space_tools_projmanag_2.GitHub Issues": 1844,
#         "space_tools_projmanag_2.GitLab": 1845,
#         "space_tools_projmanag_2.Azure DevOps": 1846,
#         "space_tools_projmanag_2.Phabricator": 1847,
#         "space_tools_projmanag_2.Basecamp": 1848,
#         "space_tools_projmanag_2.Bitrix24": 1849,
#         "space_tools_projmanag_2.Notion": 1850,
#         "space_tools_projmanag_2.Jira Software": 1851,
#         "space_tools_projmanag_2.Jira Core": 1852,
#         "space_tools_projmanag_2.Jira Align": 1853,
#         "space_tools_projmanag_2.Targetprocess": 1854,
#         "space_tools_projmanag_2.Zoho Sprints": 1855,
#         "space_tools_projmanag_2.Rally Software (CA Agile Central)": 1856,
#         "space_tools_projmanag_2.Microsoft Project": 1857,
#         "space_tools_projmanag_2.Custom tool": 1858,
#         "space_tools_projmanag_2.Other_932": 1859
#     },
#     "space_tools_vc_2": {
#         "space_tools_vc_2.None": 1764,
#         "space_tools_vc_2.Other - Write In (Required)": 1765,
#         "space_tools_vc_2.GitHub": 1766,
#         "space_tools_vc_2.GitLab": 1767,
#         "space_tools_vc_2.Bitbucket": 1768,
#         "space_tools_vc_2.Perforce": 1769,
#         "space_tools_vc_2.Amazon CodeCommit": 1770,
#         "space_tools_vc_2.SourceForge": 1771,
#         "space_tools_vc_2.Azure DevOps (former Microsoft TFS / Visual Studio Team Services)": 1772,
#         "space_tools_vc_2.Phabricator": 1773,
#         "space_tools_vc_2.Custom tool": 1774,
#         "space_tools_vc_2.Other": 1775
#     },
#     "is_employed": {
#         "is_employed": 2313
#     },
#     "primary": {
#         "primary_proglang.Java": 112,
#         "primary_proglang.C": 113,
#         "primary_proglang.C++": 114,
#         "primary_proglang.Python": 115,
#         "primary_proglang.C#": 116,
#         "primary_proglang.PHP": 117,
#         "primary_proglang.JavaScript": 118,
#         "primary_proglang.Ruby": 119,
#         "primary_proglang.Kotlin": 120,
#         "primary_proglang.Swift": 121,
#         "primary_proglang.Objective-C": 122,
#         "primary_proglang.Scala": 123,
#         "primary_proglang.Go": 124,
#         "primary_proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 125,
#         "primary_proglang.Rust": 126,
#         "primary_proglang.Haskell": 127,
#         "primary_proglang.HTML / CSS": 128,
#         "primary_proglang.Elixir": 129,
#         "primary_proglang.Visual Basic": 130,
#         "primary_proglang.R": 131,
#         "primary_proglang.TypeScript": 132,
#         "primary_proglang.Dart": 133,
#         "primary_proglang.Clojure / ClojureScript": 134,
#         "primary_proglang.Delphi": 135,
#         "primary_proglang.Groovy": 136,
#         "primary_proglang.Perl": 137,
#         "primary_proglang.Assembly": 138,
#         "primary_proglang.Matlab": 139,
#         "primary_proglang.Lua": 140,
#         "primary_proglang.Shell scripting languages(bash/shell/powershell)": 141,
#         "primary_proglang.Julia": 142,
#         "primary_proglang.F#": 143,
#         "primary_proglang.Other": 144,
#         "primary.Java": 2244,
#         "primary.JavaScript": 2246,
#         "primary.Kotlin": 2248,
#         "primary.Python": 2250,
#         "primary.C#": 2252,
#         "primary.HTML / CSS": 2254,
#         "primary.TypeScript": 2256,
#         "primary.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 2258,
#         "primary.Rust": 2260,
#         "primary.C++": 2262,
#         "primary.C": 2264,
#         "primary.Go": 2266,
#         "primary.Dart": 2268,
#         "primary.Haskell": 2270,
#         "primary.PHP": 2272,
#         "primary.Shell scripting languages(bash/shell/powershell)": 2274,
#         "primary.Swift": 2276,
#         "primary.Scala": 2278,
#         "primary.Matlab": 2280,
#         "primary.R": 2282,
#         "primary.Ruby": 2284,
#         "primary.Elixir": 2286,
#         "primary.Other": 2288,
#         "primary.Lua": 2290,
#         "primary.Visual Basic": 2292,
#         "primary.Julia": 2294,
#         "primary.Groovy": 2297,
#         "primary.Clojure / ClojureScript": 2299,
#         "primary.Objective-C": 2301,
#         "primary.Delphi": 2303,
#         "primary.Assembly": 2305,
#         "primary.F#": 2307,
#         "primary.Perl": 2310,
#         "primary.I don't use programming languages": 2312
#     },
#     "rank": {
#         "rank.Java": 2245,
#         "rank.C#": 2247,
#         "rank.PHP": 2249,
#         "rank.Python": 2251,
#         "rank.JavaScript": 2253,
#         "rank.Kotlin": 2255,
#         "rank.Scala": 2257,
#         "rank.C++": 2259,
#         "rank.TypeScript": 2261,
#         "rank.Swift": 2263,
#         "rank.Go": 2265,
#         "rank.C": 2267,
#         "rank.HTML / CSS": 2269,
#         "rank.Matlab": 2271,
#         "rank.Ruby": 2273,
#         "rank.Shell scripting languages(bash/shell/powershell)": 2275,
#         "rank.Objective-C": 2277,
#         "rank.Rust": 2279,
#         "rank.Clojure / ClojureScript": 2281,
#         "rank.Other": 2283,
#         "rank.SQL(PL/SQL, T-SQL and otherprogramming extensions of SQL)": 2285,
#         "rank.Elixir": 2287,
#         "rank.Haskell": 2289,
#         "rank.Delphi": 2291,
#         "rank.Perl": 2293,
#         "rank.Lua": 2295,
#         "rank.COBOL": 2296,
#         "rank.Groovy": 2298,
#         "rank.Dart": 2300,
#         "rank.Visual Basic": 2302,
#         "rank.R": 2304,
#         "rank.F#": 2306,
#         "rank.Assembly": 2308,
#         "rank.Julia": 2309,
#         "rank.I don't use programming languages": 2311
#     },
#     "main": {
#         "main": 2314
#     },
#     "source": {
#         "source": 2315
#     }
# }
