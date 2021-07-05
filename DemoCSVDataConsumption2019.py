import json

from pyjetbrainsdevecosystem.data_import_utils import unpack_csv_data

questions_dict = {}
with open('survey_data/2019/DevEcosystem 2019 questions_outside.csv',
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
with open('survey_data/2019/sharing_data_outside2019.csv',
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
#         "os_devenv.Unix / Linux": 20,
#         "os_devenv.macOS": 21,
#         "os_devenv.Other": 22
#     },
#     "app_type_money": {
#         "app_type_money.I don't develop anything for money": 23,
#         "app_type_money.Web Back-end": 24,
#         "app_type_money.Web Front-end": 25,
#         "app_type_money.Mobile applications": 26,
#         "app_type_money.Desktop": 27,
#         "app_type_money.Data analysis": 28,
#         "app_type_money.BI": 29,
#         "app_type_money.Machine learning": 30,
#         "app_type_money.Libraries / Frameworks": 31,
#         "app_type_money.Embedded / IoT": 32,
#         "app_type_money.Games": 33,
#         "app_type_money.Other Back-end": 34,
#         "app_type_money.Other": 35
#     },
#     "dev_for_mobile_os": {
#         "dev_for_mobile_os.Android": 76,
#         "dev_for_mobile_os.iOS": 77,
#         "dev_for_mobile_os.Other": 78
#     },
#     "db_adopt": {
#         "db_adopt.No, not planning to adopt / migrate": 270,
#         "db_adopt.Yes, planning to adopt / migrate to other database(s) - Write in": 271,
#         "db_adopt.DB2": 272,
#         "db_adopt.MS SQL Server": 273,
#         "db_adopt.MySQL": 274,
#         "db_adopt.Oracle Database": 275,
#         "db_adopt.PostgreSQL": 276,
#         "db_adopt.SQLite": 277,
#         "db_adopt.Cassandra": 278,
#         "db_adopt.Couchbase": 279,
#         "db_adopt.HBase": 280,
#         "db_adopt.MongoDB": 281,
#         "db_adopt.Neo4j": 282,
#         "db_adopt.Redis": 283,
#         "db_adopt.Amazon Redshift": 284,
#         "db_adopt.H2": 285,
#         "db_adopt.MariaDB": 286,
#         "db_adopt.ClickHouse": 287,
#         "db_adopt.Other": 288
#     },
#     "proglang": {
#         "proglang.I don't use programming languages": 97,
#         "proglang.Java": 98,
#         "proglang.C": 99,
#         "proglang.C++": 100,
#         "proglang.Python": 101,
#         "proglang.C#": 102,
#         "proglang.PHP": 103,
#         "proglang.JavaScript": 104,
#         "proglang.Ruby": 105,
#         "proglang.Elixir": 106,
#         "proglang.Crystal": 107,
#         "proglang.Kotlin": 108,
#         "proglang.Swift": 109,
#         "proglang.Objective-C": 110,
#         "proglang.Visual Basic": 111,
#         "proglang.Scala": 112,
#         "proglang.Go": 113,
#         "proglang.HTML / CSS": 114,
#         "proglang.Haskell": 115,
#         "proglang.R": 116,
#         "proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions over SQL)": 117,
#         "proglang.TypeScript": 118,
#         "proglang.Dart": 119,
#         "proglang.CoffeeScript": 120,
#         "proglang.Clojure / ClojureScript": 121,
#         "proglang.Delphi": 122,
#         "proglang.Cobol": 123,
#         "proglang.Groovy": 124,
#         "proglang.Rust": 125,
#         "proglang.Perl": 126,
#         "proglang.Assembly": 127,
#         "proglang.Matlab": 128,
#         "proglang.Lua": 129,
#         "proglang.Shell scripting languages(bash/shell/powershell)": 130,
#         "proglang.Julia": 131,
#         "proglang.F#": 132,
#         "proglang.Other": 133,
#         "proglang_rank.Java": 208,
#         "proglang_rank.C": 209,
#         "proglang_rank.C++": 210,
#         "proglang_rank.Python": 211,
#         "proglang_rank.C#": 212,
#         "proglang_rank.PHP": 213,
#         "proglang_rank.JavaScript": 214,
#         "proglang_rank.Ruby": 215,
#         "proglang_rank.Kotlin": 216,
#         "proglang_rank.Swift": 217,
#         "proglang_rank.Objective-C": 218,
#         "proglang_rank.Scala": 219,
#         "proglang_rank.Go": 220,
#         "proglang_rank.SQL(PL/SQL, T-SQL and otherprogramming extensions over SQL)": 221,
#         "proglang_rank.Rust": 222,
#         "proglang_rank.Haskell": 223,
#         "proglang_rank.HTML / CSS": 224,
#         "proglang_rank.Elixir": 225,
#         "proglang_rank.Crystal": 226,
#         "proglang_rank.Visual Basic": 227,
#         "proglang_rank.R": 228,
#         "proglang_rank.TypeScript": 229,
#         "proglang_rank.Dart": 230,
#         "proglang_rank.CoffeeScript": 231,
#         "proglang_rank.Clojure / ClojureScript": 232,
#         "proglang_rank.Delphi": 233,
#         "proglang_rank.Cobol": 234,
#         "proglang_rank.Groovy": 235,
#         "proglang_rank.Perl": 236,
#         "proglang_rank.Assembly": 237,
#         "proglang_rank.Matlab": 238,
#         "proglang_rank.Lua": 239,
#         "proglang_rank.Shell scripting languages(bash/shell/powershell)": 240,
#         "proglang_rank.Julia": 241,
#         "proglang_rank.F#": 242,
#         "proglang_rank.Other": 243
#     },
#     "tools_ci": {
#         "tools_ci.Jenkins / Hudson": 463,
#         "tools_ci.TeamCity": 464,
#         "tools_ci.Bamboo": 465,
#         "tools_ci.Microsoft Team Foundation Build": 466,
#         "tools_ci.Travis CI": 467,
#         "tools_ci.Codeship": 468,
#         "tools_ci.CircleCI": 469,
#         "tools_ci.CruiseControl": 470,
#         "tools_ci.GoCD": 471,
#         "tools_ci.Gitlab CI": 472,
#         "tools_ci.Microsoft TFS / Visual Studio Team Services": 473,
#         "tools_ci.AppVeyor": 474,
#         "tools_ci.Drone": 475,
#         "tools_ci.Semaphore CI": 476,
#         "tools_ci.Other": 477
#     },
#     "tools_it": {
#         "tools_it.Jira": 478,
#         "tools_it.YouTrack": 479,
#         "tools_it.Redmine": 480,
#         "tools_it.GitLab Issue Board": 481,
#         "tools_it.Asana": 482,
#         "tools_it.Microsoft TFS / Visual Studio Team Services": 483,
#         "tools_it.Trello": 484,
#         "tools_it.GitHub Issues": 485,
#         "tools_it.Other": 486
#     },
#     "tools_vcs": {
#         "tools_vcs.None": 492,
#         "tools_vcs.Concurrent Versions System (CVS)": 493,
#         "tools_vcs.Apache Subversion (SVN)": 494,
#         "tools_vcs.Git": 495,
#         "tools_vcs.Mercurial": 496,
#         "tools_vcs.Perforce": 497,
#         "tools_vcs.Visual Studio Team Services (VSTS)": 498,
#         "tools_vcs.Microsoft TFS": 499,
#         "tools_vcs.Other": 500
#     },
#     "contribute_os": {
#         "contribute_os.I work full time on open-source code and get paid for it": 1577,
#         "contribute_os.I work full time on open-source code but do not get paid for it": 1578,
#         "contribute_os.Yes, regularly (at least once a month)": 1579,
#         "contribute_os.Yes, from time to time (several times a year)": 1580,
#         "contribute_os.Only contributed a few times": 1581,
#         "contribute_os.No, but I would like to": 1582,
#         "contribute_os.No, and I would not like to": 1583
#     },
#     "hours_code_job": {
#         "hours_code_job": 1569
#     },
#     "tools_adopted": {
#         "tools_adopted.Source code collaboration tool (e_g_ GitHub, GitLab, Bitbucket)": 454,
#         "tools_adopted.Issue tracker (e_g_ Jira, YouTrack)": 455,
#         "tools_adopted.Code review tool (e_g_ Crucible, Upsource)": 456,
#         "tools_adopted.Continuous Integration (CI) or Continuous Delivery (CD) tool (e_g_ Jenkins, TeamCity)": 457,
#         "tools_adopted.Static analysis tool (e_g_ CodeClimate)": 458,
#         "tools_adopted.Standalone IDE (e_g_ Eclipse, IntelliJ IDEA)": 459,
#         "tools_adopted.None": 460,
#         "tools_adopted.Lightweight Desktop Editor (e_g_ Sublime Text, Atom, VS Code, Vim)": 461,
#         "tools_adopted.In-cloud Editor or IDE": 462
#     },
#     "unittests_how": {
#         "unittests_how.I write unit tests": 249,
#         "unittests_how.I use unit tests, but I don't write them": 250
#     },
#     "team_size": {
#         "team_size": 1713
#     },
#     "advocate": {
#         "advocate": 1712
#     },
#     "team_distributed": {
#         "team_distributed": 1721
#     },
#     "java_version": {
#         "java_version.Java 11": 527,
#         "java_version.Java 10": 528,
#         "java_version.Java 9": 529,
#         "java_version.Java 8": 530,
#         "java_version.Java 7": 531,
#         "java_version.Java 6": 532,
#         "java_version.Other": 533
#     },
#     "java_app_server": {
#         "java_app_server.None": 534,
#         "java_app_server.Apache Tomcat": 535,
#         "java_app_server.Jetty": 536,
#         "java_app_server.WildFly": 537,
#         "java_app_server.JBoss EAP": 538,
#         "java_app_server.WebLogic": 539,
#         "java_app_server.WebSphere": 540,
#         "java_app_server.Liberty": 541,
#         "java_app_server.GlassFish": 542,
#         "java_app_server.Payara": 543,
#         "java_app_server.Other": 544
#     },
#     "java_app_frameworks": {
#         "java_app_frameworks.None": 545,
#         "java_app_frameworks.Netty": 546,
#         "java_app_frameworks.Undertow": 547,
#         "java_app_frameworks.Vert_x": 548,
#         "java_app_frameworks.Spark Java": 549,
#         "java_app_frameworks.Spring Boot": 550,
#         "java_app_frameworks.Other": 551
#     },
#     "java_package": {
#         "java_package.As artifacts (e_g_ WAR)": 552,
#         "java_package.I use an embedded server (e_g_ JAR)": 553,
#         "java_package.I'm not sure": 554
#     },
#     "java_web_frameworks": {
#         "java_web_frameworks.None": 563,
#         "java_web_frameworks.Spring MVC": 564,
#         "java_web_frameworks.GWT": 565,
#         "java_web_frameworks.Vaadin": 566,
#         "java_web_frameworks.Play Framework": 567,
#         "java_web_frameworks.Grails 2": 568,
#         "java_web_frameworks.Grails 3": 569,
#         "java_web_frameworks.Spring Boot": 570,
#         "java_web_frameworks.JSF": 571,
#         "java_web_frameworks.Struts 1": 572,
#         "java_web_frameworks.Struts 2": 573,
#         "java_web_frameworks.Wicket": 574,
#         "java_web_frameworks.Dropwizard": 575,
#         "java_web_frameworks.Other": 576
#     },
#     "java_buildsystem": {
#         "java_buildsystem.None": 577,
#         "java_buildsystem.Maven": 578,
#         "java_buildsystem.sbt": 579,
#         "java_buildsystem.Gradle": 580,
#         "java_buildsystem.Ant": 581,
#         "java_buildsystem.Bazel": 582,
#         "java_buildsystem.Other": 583
#     },
#     "company_size": {
#         "company_size.Just me": 1649,
#         "company_size.2-10": 1650,
#         "company_size.11-50": 1651,
#         "company_size.51-500": 1652,
#         "company_size.501-1,000": 1653,
#         "company_size.1,001-5,000": 1654,
#         "company_size.More than 5,000": 1655,
#         "company_size.Not sure": 1656
#     },
#     "job_role": {
#         "job_role.Developer / Programmer /  Software Engineer": 1,
#         "job_role.DevOps Engineer / Infrastructure Developer / etc_": 2,
#         "job_role.DBA": 3,
#         "job_role.Architect": 4,
#         "job_role.Tester / QA Engineer": 5,
#         "job_role.Technical support": 6,
#         "job_role.Data analyst / Data engineer/ Data scientist": 7,
#         "job_role.Business analyst": 8,
#         "job_role.Team Lead": 9,
#         "job_role.Systems analyst": 10,
#         "job_role.Product Manager": 11,
#         "job_role.UX / UI Designer": 12,
#         "job_role.CIO / CEO / CTO": 13,
#         "job_role.Marketing Manager": 14,
#         "job_role.Developer Advocate": 15,
#         "job_role.Instructor / Teacher / Tutor / etc_": 16,
#         "job_role.Other": 17
#     },
#     "country": {
#         "country": 1736
#     },
#     "age_range": {
#         "age_range.17 or younger": 1729,
#         "age_range.18-20": 1730,
#         "age_range.21-29": 1731,
#         "age_range.30-39": 1732,
#         "age_range.40-49": 1733,
#         "age_range.50-59": 1734,
#         "age_range.60 or older": 1735
#     },
#     "adopt_proglang": {
#         "adopt_proglang.No, not planning to adopt / migrate": 170,
#         "adopt_proglang.Planning to adopt / migrate to other language(s) - Write in": 171,
#         "adopt_proglang.Java": 172,
#         "adopt_proglang.C": 173,
#         "adopt_proglang.C++": 174,
#         "adopt_proglang.Python": 175,
#         "adopt_proglang.C#": 176,
#         "adopt_proglang.PHP": 177,
#         "adopt_proglang.JavaScript": 178,
#         "adopt_proglang.Ruby": 179,
#         "adopt_proglang.Elixir": 180,
#         "adopt_proglang.Crystal": 181,
#         "adopt_proglang.Kotlin": 182,
#         "adopt_proglang.Swift": 183,
#         "adopt_proglang.Objective-C": 184,
#         "adopt_proglang.Visual Basic": 185,
#         "adopt_proglang.Scala": 186,
#         "adopt_proglang.Go": 187,
#         "adopt_proglang.HTML / CSS": 188,
#         "adopt_proglang.Haskell": 189,
#         "adopt_proglang.R": 190,
#         "adopt_proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions over SQL)": 191,
#         "adopt_proglang.TypeScript": 192,
#         "adopt_proglang.Dart": 193,
#         "adopt_proglang.CoffeeScript": 194,
#         "adopt_proglang.Clojure / ClojureScript": 195,
#         "adopt_proglang.Delphi": 196,
#         "adopt_proglang.Cobol": 197,
#         "adopt_proglang.Groovy": 198,
#         "adopt_proglang.Rust": 199,
#         "adopt_proglang.Ceylon": 200,
#         "adopt_proglang.Perl": 201,
#         "adopt_proglang.Assembly": 202,
#         "adopt_proglang.Matlab": 203,
#         "adopt_proglang.Lua": 204,
#         "adopt_proglang.Shell scripting languages(bash/shell/powershell)": 205,
#         "adopt_proglang.Julia": 206,
#         "adopt_proglang.F#": 207
#     },
#     "cloud_services": {
#         "cloud_services.Amazon Web Services": 1548,
#         "cloud_services.Microsoft Azure": 1549,
#         "cloud_services.Google Cloud Platform": 1550,
#         "cloud_services.Rackspace": 1551,
#         "cloud_services.RedHat OpenShift": 1552,
#         "cloud_services.IBM SoftLayer": 1553,
#         "cloud_services.Cloud Foundry": 1554,
#         "cloud_services.Heroku": 1555,
#         "cloud_services.Other": 1556
#     },
#     "tools_cloud": {
#         "tools_cloud.None": 487,
#         "tools_cloud.Continuous Integration tool": 488,
#         "tools_cloud.Continuous Delivery tool": 489,
#         "tools_cloud.Code Review tool": 490,
#         "tools_cloud.Issue Tracker": 491
#     },
#     "where_sources": {
#         "where_sources.Version control as a service (e_g_ GitHub, Bitbucket)": 501,
#         "where_sources.Manually deployed version control (e_g_ GitHub Enterprise, GitLab)": 502,
#         "where_sources.Other": 503
#     },
#     "vc_service": {
#         "vc_service.None": 504,
#         "vc_service.GitHub": 505,
#         "vc_service.GitLab": 506,
#         "vc_service.Bitbucket": 507,
#         "vc_service.Perforce": 508,
#         "vc_service.Amazon CodeCommit": 509,
#         "vc_service.SourceForge": 510,
#         "vc_service.Custom tool": 511,
#         "vc_service.Microsoft TFS / Visual Studio Team Services": 512,
#         "vc_service.Other": 513
#     },
#     "ide_customise": {
#         "ide_customise.No": 520,
#         "ide_customise.Yes, I use custom color schemes": 521,
#         "ide_customise.Yes, I use custom keymaps": 522,
#         "ide_customise.Yes, I use plugins": 523,
#         "ide_customise.Other": 524
#     },
#     "java_ee": {
#         "java_ee.None": 584,
#         "java_ee.Java EE 8": 585,
#         "java_ee.Java EE 7": 586,
#         "java_ee.Java EE 6": 587,
#         "java_ee.Java EE 5": 588,
#         "java_ee.J2SE": 589,
#         "java_ee.Other": 590
#     },
#     "java_profiler": {
#         "java_profiler.None": 591,
#         "java_profiler.VisualVM": 592,
#         "java_profiler.JProfiler": 593,
#         "java_profiler.Java Mission Control": 594,
#         "java_profiler.YourKit": 595,
#         "java_profiler.NetBeans profiler": 596,
#         "java_profiler.Honest profiler": 597,
#         "java_profiler.async-profiler": 598,
#         "java_profiler.Own custom tools": 599,
#         "java_profiler.Other": 600
#     },
#     "java_ide": {
#         "java_ide": 601
#     },
#     "c_standart": {
#         "c_standart.C99": 602,
#         "c_standart.C11": 603,
#         "c_standart.Embedded C": 604,
#         "c_standart.Other": 605
#     },
#     "c_ide": {
#         "c_ide": 606
#     },
#     "c_unittesting": {
#         "c_unittesting.None": 607,
#         "c_unittesting.Catch": 608,
#         "c_unittesting.Boost_Test": 609,
#         "c_unittesting.Google Test": 610,
#         "c_unittesting.CppUnit": 611,
#         "c_unittesting.CppUTest": 612,
#         "c_unittesting.CUnit": 613,
#         "c_unittesting.Unity": 614,
#         "c_unittesting.Other": 615
#     },
#     "c_projectmodels": {
#         "c_projectmodels.None": 616,
#         "c_projectmodels.Visual Studio project": 617,
#         "c_projectmodels.Xcode project": 618,
#         "c_projectmodels.Autotools": 619,
#         "c_projectmodels.Makefiles": 620,
#         "c_projectmodels.CMake": 621,
#         "c_projectmodels.Qmake": 622,
#         "c_projectmodels.Custom": 623,
#         "c_projectmodels.Other": 624
#     },
#     "c_compilers": {
#         "c_compilers.GCC": 632,
#         "c_compilers.Clang": 633,
#         "c_compilers.MSVC": 634,
#         "c_compilers.Intel": 635,
#         "c_compilers.Compiler for microcontrollers (like Keil, C51 C Compiler, IAR, etc_)": 636,
#         "c_compilers.Custom": 637,
#         "c_compilers.Other": 638
#     },
#     "cpp_standart": {
#         "cpp_standart.C++98": 639,
#         "cpp_standart.C++03": 640,
#         "cpp_standart.C++11": 641,
#         "cpp_standart.C++14": 642,
#         "cpp_standart.C++17": 643,
#         "cpp_standart_migrate.No, I don't plan to": 644,
#         "cpp_standart_migrate.C++98": 645,
#         "cpp_standart_migrate.C++11": 646,
#         "cpp_standart_migrate.C++14": 647,
#         "cpp_standart_migrate.\u0421++17": 648
#     },
#     "cpp_standart_migrate": {
#         "cpp_standart_migrate.No, I don't plan to": 644,
#         "cpp_standart_migrate.C++98": 645,
#         "cpp_standart_migrate.C++11": 646,
#         "cpp_standart_migrate.C++14": 647,
#         "cpp_standart_migrate.\u0421++17": 648
#     },
#     "cpp_ide": {
#         "cpp_ide.Visual Studio": 651,
#         "cpp_ide.Visual Studio Code": 652,
#         "cpp_ide.NetBeans": 653,
#         "cpp_ide.Eclipse CDT": 654,
#         "cpp_ide.QtCreator": 655,
#         "cpp_ide.CLion": 656,
#         "cpp_ide.Xcode": 657,
#         "cpp_ide.Atom": 658,
#         "cpp_ide.Sublime": 659,
#         "cpp_ide.Vi/Vim": 660,
#         "cpp_ide.Emacs": 661,
#         "cpp_ide.Other": 662
#     },
#     "cpp_unittesting": {
#         "cpp_unittesting.None": 663,
#         "cpp_unittesting.Boost_Test": 664,
#         "cpp_unittesting.Google Test": 665,
#         "cpp_unittesting.CppUnit": 666,
#         "cpp_unittesting.CppUTest": 667,
#         "cpp_unittesting.Catch": 668,
#         "cpp_unittesting.Other": 669
#     },
#     "cpp_projectmodels": {
#         "cpp_projectmodels.None": 678,
#         "cpp_projectmodels.Visual Studio project": 679,
#         "cpp_projectmodels.Xcode project": 680,
#         "cpp_projectmodels.Autotools": 681,
#         "cpp_projectmodels.Makefiles": 682,
#         "cpp_projectmodels.CMake": 683,
#         "cpp_projectmodels.Qmake": 684,
#         "cpp_projectmodels.SCons": 685,
#         "cpp_projectmodels.Boost_Build": 686,
#         "cpp_projectmodels.Bazel": 687,
#         "cpp_projectmodels.Custom": 688,
#         "cpp_projectmodels.Other": 689
#     },
#     "cpp_compilers": {
#         "cpp_compilers.GCC": 690,
#         "cpp_compilers.Clang": 691,
#         "cpp_compilers.MSVC": 692,
#         "cpp_compilers.Intel": 693,
#         "cpp_compilers.Custom": 694,
#         "cpp_compilers.Other": 695
#     },
#     "cpp_cli": {
#         "cpp_cli.Yes": 649,
#         "cpp_cli.No": 650
#     },
#     "cpp_project_size": {
#         "cpp_project_size.Small / Medium projects with most commonly used C++ (C++11) features": 723,
#         "cpp_project_size.Small / Medium projects with heavy use of templates/variadic templates and other C++11/14/17 features": 724,
#         "cpp_project_size.Big / Huge projects with many lines of code, libraries, etc_ but only using the most common C++ (C++11) features": 725,
#         "cpp_project_size.Big / Huge projects with many lines of code, libraries, etc_, with heavy use of templates/variadic templates, and other C++11/14/17 features": 726,
#         "cpp_project_size.Other": 727
#     },
#     "python_vesion": {
#         "python_vesion.Python 2": 728,
#         "python_vesion.Python 3": 729
#     },
#     "python_ide": {
#         "python_ide.PyCharm Professional Edition": 790,
#         "python_ide.PyCharm Community Edition": 791,
#         "python_ide.VS Code": 792,
#         "python_ide.Sublime Text": 793,
#         "python_ide.Vim": 794,
#         "python_ide.IntelliJ IDEA": 795,
#         "python_ide.Atom": 796,
#         "python_ide.Emacs": 797,
#         "python_ide.Eclipse + Pydev": 798,
#         "python_ide.IPython Notebook": 799,
#         "python_ide.Jupyter Notebook": 800,
#         "python_ide.NotePad++": 801,
#         "python_ide.Spyder": 802,
#         "python_ide.IDLE": 803,
#         "python_ide.Other": 804
#     },
#     "csharp_version": {
#         "csharp_version.C# 5 (async / await, caller info attributes)": 805,
#         "csharp_version.C# 6 (? and nameof operators, static imports, exception filters, Roslyn)": 806,
#         "csharp_version.C# 7 (pattern matching, local functions, ref locals and returns, out variables)": 807,
#         "csharp_version.An earlier version": 808,
#         "csharp_version.I'm not sure": 809
#     },
#     "csharp_runtimes": {
#         "csharp_runtimes._NET Framework": 810,
#         "csharp_runtimes.Mono": 811,
#         "csharp_runtimes._NET Core": 812
#     },
#     "csharp_frameworks": {
#         "csharp_frameworks.None": 813,
#         "csharp_frameworks.Sharepoint": 814,
#         "csharp_frameworks.ASP_NET MVC": 815,
#         "csharp_frameworks.ASP_NET Web Forms": 816,
#         "csharp_frameworks.ASP_NET Core": 817,
#         "csharp_frameworks.Windows Presentation Foundation (WPF)": 818,
#         "csharp_frameworks.Windows Forms": 819,
#         "csharp_frameworks.Windows Communication Foundation (WCF)": 820,
#         "csharp_frameworks.Entity Framework": 821,
#         "csharp_frameworks.Unity3d": 822,
#         "csharp_frameworks.Xamarin": 823,
#         "csharp_frameworks.UWP": 824,
#         "csharp_frameworks.Azure": 825,
#         "csharp_frameworks.Other": 826
#     },
#     "csharp_ide": {
#         "csharp_ide": 827
#     },
#     "csharp_vsversion": {
#         "csharp_vsversion": 850
#     },
#     "csharp_unittesting": {
#         "csharp_unittesting.None": 852,
#         "csharp_unittesting.MSTest/Visual Studio Unit Testing Framework": 853,
#         "csharp_unittesting.MSTest V2": 854,
#         "csharp_unittesting.NUnit": 855,
#         "csharp_unittesting.xUnit": 856,
#         "csharp_unittesting.Other": 857
#     },
#     "csharp_performance": {
#         "csharp_performance.None": 858,
#         "csharp_performance.PerfView": 859,
#         "csharp_performance.Intel VTune Amplifier": 860,
#         "csharp_performance.SciTech _NET memory profiler": 861,
#         "csharp_performance.Windows Performance Toolkit": 862,
#         "csharp_performance.Visual Studio's built-in performance and diagnostic tools": 863,
#         "csharp_performance.dotTrace": 864,
#         "csharp_performance.dotMemory": 865,
#         "csharp_performance.ANTS Profiler": 866,
#         "csharp_performance.Other": 867
#     },
#     "php_version": {
#         "php_version.PHP 7_3": 873,
#         "php_version.PHP 7_2": 874,
#         "php_version.PHP 7_1": 875,
#         "php_version.PHP 7_0": 876,
#         "php_version.PHP 5_6": 877,
#         "php_version.PHP 5_5": 878,
#         "php_version.PHP 5_4": 879,
#         "php_version.PHP 5_3": 880,
#         "php_version.Other": 881
#     },
#     "php_devenviron": {
#         "php_devenviron.Local": 882,
#         "php_devenviron.Remote (SFTP, SSH, Remote desktop, etc_)": 883,
#         "php_devenviron.Virtualized  (Vagrant, Otto, etc_)": 884,
#         "php_devenviron.Containerized (Docker, Rocket)": 885,
#         "php_devenviron.Other": 886
#     },
#     "php_debugger": {
#         "php_debugger": 887
#     },
#     "php_ide": {
#         "php_ide.Atom": 901,
#         "php_ide.Eclipse PDT": 902,
#         "php_ide.NetBeans IDE": 903,
#         "php_ide.Notepad++": 904,
#         "php_ide.PHPEdit": 905,
#         "php_ide.PhpStorm": 906,
#         "php_ide.Sublime Text": 907,
#         "php_ide.Vim": 908,
#         "php_ide.VS Code": 909,
#         "php_ide.IntelliJ IDEA Ultimate with PHP plugin": 910,
#         "php_ide.Other": 911
#     },
#     "php_testing": {
#         "php_testing.None": 912,
#         "php_testing.PHPUnit": 913,
#         "php_testing.Behat": 914,
#         "php_testing.PHPSpec": 915,
#         "php_testing.Codeception": 916,
#         "php_testing.Atoum": 917,
#         "php_testing.SimpleTest": 918,
#         "php_testing.Other": 919
#     },
#     "js_frameworks": {
#         "js_frameworks.None": 1231,
#         "js_frameworks.AngularJS": 1232,
#         "js_frameworks.Angular": 1233,
#         "js_frameworks.React": 1234,
#         "js_frameworks.React Native": 1235,
#         "js_frameworks.Cordova / PhoneGap": 1236,
#         "js_frameworks.Express": 1237,
#         "js_frameworks.Vue_js": 1238,
#         "js_frameworks.Meteor": 1239,
#         "js_frameworks.Ember": 1240,
#         "js_frameworks.Backbone": 1241,
#         "js_frameworks.Polymer": 1242,
#         "js_frameworks.Electron": 1243,
#         "js_frameworks.Other": 1244
#     },
#     "js_ide": {
#         "js_ide.WebStorm (or another JetBrains IDE)": 1245,
#         "js_ide.Sublime Text": 1246,
#         "js_ide.Atom": 1247,
#         "js_ide.VS Code": 1248,
#         "js_ide.Vi / Vim": 1249,
#         "js_ide.Visual Studio": 1250,
#         "js_ide.NotePad++": 1251,
#         "js_ide.Emacs": 1252,
#         "js_ide.Other": 1253
#     },
#     "js_unittesting": {
#         "js_unittesting.None": 1254,
#         "js_unittesting.Mocha": 1255,
#         "js_unittesting.Jest": 1256,
#         "js_unittesting.Ava": 1257,
#         "js_unittesting.Karma": 1258,
#         "js_unittesting.Jasmine": 1259,
#         "js_unittesting.Other": 1260
#     },
#     "js_moduleloader": {
#         "js_moduleloader.None": 1261,
#         "js_moduleloader.Browserify": 1262,
#         "js_moduleloader.Webpack": 1263,
#         "js_moduleloader.RequireJS": 1264,
#         "js_moduleloader.SystemJS": 1265,
#         "js_moduleloader.Rollup": 1266,
#         "js_moduleloader.Parcel": 1267,
#         "js_moduleloader.Other": 1268
#     },
#     "ruby_version": {
#         "ruby_version.Ruby 2_6": 1053,
#         "ruby_version.Ruby 2_5": 1054,
#         "ruby_version.Ruby 2_4": 1055,
#         "ruby_version.Ruby 2_3": 1056,
#         "ruby_version.Ruby 2_2": 1057,
#         "ruby_version.Ruby 2_1": 1058,
#         "ruby_version.Ruby 2_0": 1059,
#         "ruby_version.Ruby 1_9": 1060,
#         "ruby_version.Ruby 1_8": 1061,
#         "ruby_version.Other": 1062,
#         "ruby_version_management.None": 1063,
#         "ruby_version_management.RVM": 1064,
#         "ruby_version_management.Rbenv": 1065,
#         "ruby_version_management.Asdf": 1066,
#         "ruby_version_management.Chruby": 1067,
#         "ruby_version_management.Docker": 1068,
#         "ruby_version_management.Other": 1069
#     },
#     "ruby_gemmanagement": {
#         "ruby_gemmanagement.None": 1070,
#         "ruby_gemmanagement.Bundler": 1071,
#         "ruby_gemmanagement.RVM gemsets": 1072,
#         "ruby_gemmanagement.Rbenv gemsets": 1073,
#         "ruby_gemmanagement.Other": 1074
#     },
#     "ruby_gems_count": {
#         "ruby_gems_count": 1075
#     },
#     "ruby_frameworks": {
#         "ruby_frameworks.None": 1076,
#         "ruby_frameworks.Ruby on Rails": 1077,
#         "ruby_frameworks.Rack": 1078,
#         "ruby_frameworks.Sinatra": 1079,
#         "ruby_frameworks.Padrino": 1080,
#         "ruby_frameworks.Hanami": 1081,
#         "ruby_frameworks.Hyperstack": 1082,
#         "ruby_frameworks.Opal": 1083,
#         "ruby_frameworks.Other": 1084
#     },
#     "ruby_rails_version": {
#         "ruby_rails_version": 1085,
#         "ruby_rails_version_migrate": 1086
#     },
#     "ruby_servers": {
#         "ruby_servers.None": 1087,
#         "ruby_servers.Unicorn": 1088,
#         "ruby_servers.Puma": 1089,
#         "ruby_servers.Passenger": 1090,
#         "ruby_servers.Thin": 1091,
#         "ruby_servers.Other": 1092
#     },
#     "ruby_ide": {
#         "ruby_ide": 1093
#     },
#     "ruby_unittesting": {
#         "ruby_unittesting.None": 1094,
#         "ruby_unittesting.Shoulda": 1095,
#         "ruby_unittesting.RSpec": 1096,
#         "ruby_unittesting.Cucumber": 1097,
#         "ruby_unittesting.MiniTest": 1098,
#         "ruby_unittesting.TestUnit": 1099,
#         "ruby_unittesting.Other": 1100
#     },
#     "swiftoc_unittesting": {
#         "swiftoc_unittesting.None": 1108,
#         "swiftoc_unittesting.XCTest": 1109,
#         "swiftoc_unittesting.Quick + Nimble": 1110,
#         "swiftoc_unittesting.Kiwi": 1111,
#         "swiftoc_unittesting.Specta": 1112,
#         "swiftoc_unittesting.Other": 1113
#     },
#     "swiftoc_ui_tests": {
#         "swiftoc_ui_tests": 1122
#     },
#     "swiftoc_dependecymanager": {
#         "swiftoc_dependecymanager.None": 1129,
#         "swiftoc_dependecymanager.CocoaPods": 1130,
#         "swiftoc_dependecymanager.Carthage": 1131,
#         "swiftoc_dependecymanager.Swift Package Manager": 1132,
#         "swiftoc_dependecymanager.Other": 1133
#     },
#     "swiftoc_db_engine": {
#         "swiftoc_db_engine.None": 1134,
#         "swiftoc_db_engine.SQLite with my own wrapper": 1135,
#         "swiftoc_db_engine.CoreData": 1136,
#         "swiftoc_db_engine.Realm": 1137,
#         "swiftoc_db_engine.Firebase": 1138,
#         "swiftoc_db_engine.YAPDataBase": 1139,
#         "swiftoc_db_engine.Other": 1140
#     },
#     "swiftoc_build": {
#         "swiftoc_build.I build my project from the IDE": 1143,
#         "swiftoc_build.I use Fastlane": 1144,
#         "swiftoc_build.I build on CI": 1145,
#         "swiftoc_build.Other": 1146
#     },
#     "swiftoc_linux": {
#         "swiftoc_linux.Yes": 1147,
#         "swiftoc_linux.No, but I plan to in the next 12 months": 1148,
#         "swiftoc_linux.No, and I don\u2019t plan to in the next 12 months": 1149
#     },
#     "sql_mssql": {
#         "sql_mssql.2017": 1364,
#         "sql_mssql.2016": 1365,
#         "sql_mssql.2014": 1366,
#         "sql_mssql.2012": 1367,
#         "sql_mssql.2008 R2": 1368,
#         "sql_mssql.2008": 1369,
#         "sql_mssql.2005": 1370,
#         "sql_mssql.2000": 1371,
#         "sql_mssql.I'm not sure": 1372
#     },
#     "sql_mysql": {
#         "sql_mysql.8_0": 1380,
#         "sql_mysql.5_7": 1381,
#         "sql_mysql.5_6": 1382,
#         "sql_mysql.5_5": 1383,
#         "sql_mysql.5_4": 1384,
#         "sql_mysql.I'm not sure": 1385,
#         "sql_mysql.Other": 1386
#     },
#     "sql_postgresql": {
#         "sql_postgresql.11": 1387,
#         "sql_postgresql.10": 1388,
#         "sql_postgresql.9_6": 1389,
#         "sql_postgresql.9_5": 1390,
#         "sql_postgresql.9_4": 1391,
#         "sql_postgresql.9_3": 1392,
#         "sql_postgresql.9_2": 1393,
#         "sql_postgresql.9_1": 1394,
#         "sql_postgresql.9_0": 1395,
#         "sql_postgresql.I'm not sure": 1396,
#         "sql_postgresql.Other": 1397
#     },
#     "sql_db2": {
#         "sql_db2.11_x": 1398,
#         "sql_db2.10_x": 1399,
#         "sql_db2.9_x": 1400,
#         "sql_db2.8_x": 1401,
#         "sql_db2.7_x": 1402,
#         "sql_db2.Other": 1403
#     },
#     "sql_sqlite": {
#         "sql_sqlite": 1404
#     },
#     "sql_tool": {
#         "sql_tool.None": 1405,
#         "sql_tool.MySQL Workbench": 1406,
#         "sql_tool.pgAdmin": 1407,
#         "sql_tool.Oracle SQL Developer": 1408,
#         "sql_tool.SQL Server Management Studio": 1409,
#         "sql_tool.DataGrip": 1410,
#         "sql_tool.phpMyAdmin": 1411,
#         "sql_tool.Navicat": 1412,
#         "sql_tool.Toad": 1413,
#         "sql_tool.EMS SQL Manager": 1414,
#         "sql_tool.dbForge Studio": 1415,
#         "sql_tool.HeidiSQL": 1416,
#         "sql_tool.DbVisualizer": 1417,
#         "sql_tool.DBeaver": 1418,
#         "sql_tool.Sequel Pro": 1419,
#         "sql_tool.SQuirreL SQL": 1420,
#         "sql_tool.Command Line": 1421,
#         "sql_tool.JetBrains IDE(s) (IntelliJ IDEA, PhpStorm, etc_) with the Database plugin": 1422,
#         "sql_tool.Robo 3T": 1423,
#         "sql_tool.PL / SQL Developer": 1424,
#         "sql_tool.Other": 1425
#     },
#     "use_static_analysis": {
#         "use_static_analysis": 1568
#     },
#     "regularly_tools": {
#         "regularly_tools.Source code collaboration tool (e_g_ GitHub, GitLab, Bitbucket)": 342,
#         "regularly_tools.Issue tracker (e_g_ Jira, YouTrack)": 343,
#         "regularly_tools.Code review tool (e_g_ Crucible, Upsource)": 344,
#         "regularly_tools.Continuous Integration (CI) or Continuous Delivery (CD) tool (e_g_ Jenkins, TeamCity)": 345,
#         "regularly_tools.Static analysis tool (e_g_ CodeClimate)": 346,
#         "regularly_tools.Standalone IDE (e_g_ Eclipse, IntelliJ IDEA)": 347,
#         "regularly_tools.Lightweight Desktop Editor (e_g_ Sublime Text, Atom, VS Code, Vim)": 348,
#         "regularly_tools.In-cloud Editor or IDE": 349,
#         "regularly_tools.None": 350
#     },
#     "visit_meetups": {
#         "visit_meetups.Yes": 1611,
#         "visit_meetups.No, but I am planning to": 1612,
#         "visit_meetups.No, since there are no meetups in my area": 1613,
#         "visit_meetups.No, I am unable to do so for certain reasons": 1614,
#         "visit_meetups.No, and I do not want to": 1615,
#         "visit_meetups.Other": 1616
#     },
#     "it_experience": {
#         "it_experience.None": 1722,
#         "it_experience.Less than 1 year": 1723,
#         "it_experience.1 - 2 years": 1724,
#         "it_experience.3 - 5 years": 1725,
#         "it_experience.6 - 10 years": 1726,
#         "it_experience.11+ years": 1727
#     },
#     "ruby_rails_version_migrate": {
#         "ruby_rails_version_migrate": 1086
#     },
#     "scala_java_version": {
#         "scala_java_version.Java 11": 1163,
#         "scala_java_version.Java 10": 1164,
#         "scala_java_version.Java 9": 1165,
#         "scala_java_version.Java 8": 1166,
#         "scala_java_version.Java 7": 1167,
#         "scala_java_version.Other": 1168
#     },
#     "scala_frameworks_web": {
#         "scala_frameworks_web.None": 1178,
#         "scala_frameworks_web.Akka-http": 1179,
#         "scala_frameworks_web.Netty": 1180,
#         "scala_frameworks_web.Spark Java": 1181,
#         "scala_frameworks_web.Play": 1182,
#         "scala_frameworks_web.Spray": 1183,
#         "scala_frameworks_web.Scalatra": 1184,
#         "scala_frameworks_web.Finatra": 1185,
#         "scala_frameworks_web.Spring": 1186,
#         "scala_frameworks_web.sttp": 1187,
#         "scala_frameworks_web.Http4s": 1188,
#         "scala_frameworks_web.Other": 1189
#     },
#     "scala_ide": {
#         "scala_ide.IntelliJ IDEA": 1204,
#         "scala_ide.Other": 1205
#     },
#     "scala_buildsystem": {
#         "scala_buildsystem.Maven": 1206,
#         "scala_buildsystem.Gradle": 1207,
#         "scala_buildsystem.sbt": 1208,
#         "scala_buildsystem.Other": 1209
#     },
#     "scala_macros": {
#         "scala_macros.Yes, including whitebox macros": 1226,
#         "scala_macros.Only blackbox macros": 1227,
#         "scala_macros.Only in libraries": 1228,
#         "scala_macros.No": 1229,
#         "scala_macros.I don\u2019t know anything about macros in Scala": 1230
#     },
#     "dev_for_desk_os": {
#         "dev_for_desk_os.Windows": 49,
#         "dev_for_desk_os.Unix / Linux": 50,
#         "dev_for_desk_os.macOS": 51,
#         "dev_for_desk_os.Other": 52
#     },
#     "php_frameworks": {
#         "php_frameworks.None": 888,
#         "php_frameworks.Symfony": 889,
#         "php_frameworks.Drupal": 890,
#         "php_frameworks.WordPress": 891,
#         "php_frameworks.Zend": 892,
#         "php_frameworks.Magento": 893,
#         "php_frameworks.Laravel": 894,
#         "php_frameworks.Joomla!": 895,
#         "php_frameworks.Yii": 896,
#         "php_frameworks.CakePHP": 897,
#         "php_frameworks.CodeIgniter": 898,
#         "php_frameworks.Slim": 899,
#         "php_frameworks.Other": 900
#     },
#     "devops_conf_management": {
#         "devops_conf_management.None": 1485,
#         "devops_conf_management.Puppet": 1486,
#         "devops_conf_management.Chef": 1487,
#         "devops_conf_management.Ansible": 1488,
#         "devops_conf_management.Salt": 1489,
#         "devops_conf_management.Custom solution": 1490,
#         "devops_conf_management.Other": 1491
#     },
#     "ruby_version_management": {
#         "ruby_version_management.None": 1063,
#         "ruby_version_management.RVM": 1064,
#         "ruby_version_management.Rbenv": 1065,
#         "ruby_version_management.Asdf": 1066,
#         "ruby_version_management.Chruby": 1067,
#         "ruby_version_management.Docker": 1068,
#         "ruby_version_management.Other": 1069
#     },
#     "agile_framework": {
#         "agile_framework.None": 1714,
#         "agile_framework.Scrum": 1715,
#         "agile_framework.Kanban": 1716,
#         "agile_framework.XP": 1717,
#         "agile_framework.Combined": 1718,
#         "agile_framework.Other": 1719
#     },
#     "hours_code_hobby": {
#         "hours_code_hobby.I don\u2019t have a side project": 1570,
#         "hours_code_hobby.Less than 1 hour a week": 1571,
#         "hours_code_hobby.1-2 hours a week": 1572,
#         "hours_code_hobby.3-8 hours a week": 1573,
#         "hours_code_hobby.9-16 hours a week": 1574,
#         "hours_code_hobby.17-32 hours a week": 1575,
#         "hours_code_hobby.32 hours a week or more": 1576
#     },
#     "code_weekends": {
#         "code_weekends.Yes": 1585,
#         "code_weekends.No": 1586
#     },
#     "app_type_hobby": {
#         "app_type_hobby.I don't develop anything for free / only as a hobby": 36,
#         "app_type_hobby.Web Back-end": 37,
#         "app_type_hobby.Web Front-end": 38,
#         "app_type_hobby.Mobile applications": 39,
#         "app_type_hobby.Desktop": 40,
#         "app_type_hobby.Data analysis": 41,
#         "app_type_hobby.BI": 42,
#         "app_type_hobby.Machine learning": 43,
#         "app_type_hobby.Embedded / IoT": 44,
#         "app_type_hobby.Games": 45,
#         "app_type_hobby.Libraries / Frameworks": 46,
#         "app_type_hobby.Other Back-end": 47,
#         "app_type_hobby.Other": 48
#     },
#     "ides": {
#         "ides.RStudio": 351,
#         "ides.IntelliJ IDEA": 352,
#         "ides.Android Studio": 353,
#         "ides.Visual Studio": 354,
#         "ides.Xcode": 355,
#         "ides.PhpStorm": 356,
#         "ides.WebStorm": 357,
#         "ides.RubyMine": 358,
#         "ides.PyCharm": 359,
#         "ides.Vim": 360,
#         "ides.Sublime Text": 361,
#         "ides.Atom": 362,
#         "ides.VS Code (Visual Studio Code)": 363,
#         "ides.Notepad++": 364,
#         "ides.AppCode": 365,
#         "ides.CLion": 366,
#         "ides.Eclipse": 367,
#         "ides.NetBeans": 368,
#         "ides.QtCreator": 369,
#         "ides.Emacs": 370,
#         "ides.JetBrains Rider": 371,
#         "ides.Gedit": 372,
#         "ides.IPython/Jupyter Notebook": 373,
#         "ides.DataGrip": 374,
#         "ides.GoLand": 375,
#         "ides.Other": 376
#     },
#     "mobile_os_how": {
#         "mobile_os_how.I use native tools (Swift / Objective-C for iOS, Kotlin / Android, etc)": 79,
#         "mobile_os_how.I use cross-platform technologies / frameworks (Xamarin, Apache Cordova, Ionic, etc)": 80
#     },
#     "crossplatform_framework": {
#         "crossplatform_framework.Apache Flex": 81,
#         "crossplatform_framework.Corona": 82,
#         "crossplatform_framework.Ionic": 83,
#         "crossplatform_framework.Kivy": 84,
#         "crossplatform_framework.Sencha": 85,
#         "crossplatform_framework.Dojo": 86,
#         "crossplatform_framework.Titanium": 87,
#         "crossplatform_framework.Kendo UI": 88,
#         "crossplatform_framework.Xamarin": 89,
#         "crossplatform_framework.Cordova": 90,
#         "crossplatform_framework.Unity": 91,
#         "crossplatform_framework.React Native": 92,
#         "crossplatform_framework.Flutter": 93,
#         "crossplatform_framework.PhoneGap": 94,
#         "crossplatform_framework.NativeScript": 95,
#         "crossplatform_framework.Other": 96
#     },
#     "python_for": {
#         "python_for.Educational purposes": 730,
#         "python_for.Data analysis": 731,
#         "python_for.System administration / Writing automation scripts / Infrastructure configuration (DevOps)": 732,
#         "python_for.Software testing / writing automated tests": 733,
#         "python_for.Software prototyping": 734,
#         "python_for.Web development": 735,
#         "python_for.Programming of web parsers / scrapers / crawlers": 736,
#         "python_for.Machine learning": 737,
#         "python_for.Network programming": 738,
#         "python_for.Desktop development": 739,
#         "python_for.Computer graphics": 740,
#         "python_for.Game development": 741,
#         "python_for.Mobile development": 742,
#         "python_for.Embedded development": 743,
#         "python_for.Other": 744
#     },
#     "csharp_os": {
#         "csharp_os.Windows": 835,
#         "csharp_os.Unix / Linux": 836,
#         "csharp_os.macOS": 837,
#         "csharp_os.Other": 838
#     },
#     "csharp_vsc_plugins": {
#         "csharp_vsc_plugins.None": 839,
#         "csharp_vsc_plugins.C# for Visual Studio Code (powered by OmniSharp)": 840,
#         "csharp_vsc_plugins.NuGet Package Manager": 841,
#         "csharp_vsc_plugins.C# Extensions": 842,
#         "csharp_vsc_plugins.C# XML Documentation Comments": 843,
#         "csharp_vsc_plugins.Code Runner": 844,
#         "csharp_vsc_plugins.ESLint": 845,
#         "csharp_vsc_plugins.TSLint": 846,
#         "csharp_vsc_plugins.ASP_NET Helper": 847,
#         "csharp_vsc_plugins.C# snippets": 848,
#         "csharp_vsc_plugins.Other": 849
#     },
#     "csharp_msdn": {
#         "csharp_msdn": 868,
#         "csharp_msdn_type": 869
#     },
#     "csharp_tfs": {
#         "csharp_tfs.No": 870,
#         "csharp_tfs.TFS": 871,
#         "csharp_tfs.VSTS": 872
#     },
#     "scala_version": {
#         "scala_version.2_13": 1155,
#         "scala_version.2_12": 1156,
#         "scala_version.2_11": 1157,
#         "scala_version.2_10 or older": 1158,
#         "scala_version.Other": 1159
#     },
#     "scala_compilationtarget": {
#         "scala_compilationtarget.JVM": 1160,
#         "scala_compilationtarget.scala_js": 1161,
#         "scala_compilationtarget.Other": 1162
#     },
#     "scala_unittesting": {
#         "scala_unittesting.None": 1169,
#         "scala_unittesting.ScalaTest": 1170,
#         "scala_unittesting.ScalaMock": 1171,
#         "scala_unittesting.TestNG": 1172,
#         "scala_unittesting.JUnit": 1173,
#         "scala_unittesting.ScalaCheck": 1174,
#         "scala_unittesting.specs2": 1175,
#         "scala_unittesting.\u00b5Test": 1176,
#         "scala_unittesting.Other": 1177
#     },
#     "proglang_rank": {
#         "proglang_rank.Java": 208,
#         "proglang_rank.C": 209,
#         "proglang_rank.C++": 210,
#         "proglang_rank.Python": 211,
#         "proglang_rank.C#": 212,
#         "proglang_rank.PHP": 213,
#         "proglang_rank.JavaScript": 214,
#         "proglang_rank.Ruby": 215,
#         "proglang_rank.Kotlin": 216,
#         "proglang_rank.Swift": 217,
#         "proglang_rank.Objective-C": 218,
#         "proglang_rank.Scala": 219,
#         "proglang_rank.Go": 220,
#         "proglang_rank.SQL(PL/SQL, T-SQL and otherprogramming extensions over SQL)": 221,
#         "proglang_rank.Rust": 222,
#         "proglang_rank.Haskell": 223,
#         "proglang_rank.HTML / CSS": 224,
#         "proglang_rank.Elixir": 225,
#         "proglang_rank.Crystal": 226,
#         "proglang_rank.Visual Basic": 227,
#         "proglang_rank.R": 228,
#         "proglang_rank.TypeScript": 229,
#         "proglang_rank.Dart": 230,
#         "proglang_rank.CoffeeScript": 231,
#         "proglang_rank.Clojure / ClojureScript": 232,
#         "proglang_rank.Delphi": 233,
#         "proglang_rank.Cobol": 234,
#         "proglang_rank.Groovy": 235,
#         "proglang_rank.Perl": 236,
#         "proglang_rank.Assembly": 237,
#         "proglang_rank.Matlab": 238,
#         "proglang_rank.Lua": 239,
#         "proglang_rank.Shell scripting languages(bash/shell/powershell)": 240,
#         "proglang_rank.Julia": 241,
#         "proglang_rank.F#": 242,
#         "proglang_rank.Other": 243
#     },
#     "python_other_techs": {
#         "python_other_techs.None": 785,
#         "python_other_techs.Sphinx": 786,
#         "python_other_techs.Buildout": 787,
#         "python_other_techs.ORM": 788,
#         "python_other_techs.Other": 789
#     },
#     "kotlin_how_long": {
#         "kotlin_how_long": 1033
#     },
#     "scala_frameworks": {
#         "scala_frameworks_web.None": 1178,
#         "scala_frameworks_web.Akka-http": 1179,
#         "scala_frameworks_web.Netty": 1180,
#         "scala_frameworks_web.Spark Java": 1181,
#         "scala_frameworks_web.Play": 1182,
#         "scala_frameworks_web.Spray": 1183,
#         "scala_frameworks_web.Scalatra": 1184,
#         "scala_frameworks_web.Finatra": 1185,
#         "scala_frameworks_web.Spring": 1186,
#         "scala_frameworks_web.sttp": 1187,
#         "scala_frameworks_web.Http4s": 1188,
#         "scala_frameworks_web.Other": 1189,
#         "scala_frameworks.None": 1190,
#         "scala_frameworks.Scala_js": 1191,
#         "scala_frameworks.Twitter Util": 1192,
#         "scala_frameworks.Akka": 1193,
#         "scala_frameworks.Spark": 1194,
#         "scala_frameworks.Scalaz": 1195,
#         "scala_frameworks.Scalacheck": 1196,
#         "scala_frameworks.Specs2": 1197,
#         "scala_frameworks.Shapeless": 1198,
#         "scala_frameworks.Finagle": 1199,
#         "scala_frameworks.Cats": 1200,
#         "scala_frameworks.Breeze": 1201,
#         "scala_frameworks.Slick": 1202,
#         "scala_frameworks.Other": 1203
#     },
#     "scala_sbt": {
#         "scala_sbt.1_0": 1210,
#         "scala_sbt.0_13 or older": 1211
#     },
#     "scala_interactive": {
#         "scala_interactive.None": 1212,
#         "scala_interactive.Scala REPL": 1213,
#         "scala_interactive.sbt console": 1214,
#         "scala_interactive.Ammonite REPL": 1215,
#         "scala_interactive.Scastie": 1216,
#         "scala_interactive.IntelliJ IDEA Worksheet": 1217,
#         "scala_interactive.Scala IDE Worksheet": 1218,
#         "scala_interactive.Apache Zeppelin Notebook": 1219,
#         "scala_interactive.Jupyter Notebook": 1220,
#         "scala_interactive.Other": 1221
#     },
#     "scala_compiler_plugins": {
#         "scala_compiler_plugins.None": 1222,
#         "scala_compiler_plugins.Scalamacros/Scalameta Paradise": 1223,
#         "scala_compiler_plugins.Kind Projector": 1224,
#         "scala_compiler_plugins.Other": 1225
#     },
#     "go_multipleversions": {
#         "go_multipleversions": 1427
#     },
#     "go_gopath": {
#         "go_gopath": 1428
#     },
#     "go_multipleprojects": {
#         "go_multipleprojects": 1429
#     },
#     "go_packagemanager": {
#         "go_packagemanager.None": 1436,
#         "go_packagemanager.dep": 1437,
#         "go_packagemanager.godep": 1438,
#         "go_packagemanager.glide": 1439,
#         "go_packagemanager.govendor": 1440,
#         "go_packagemanager.Go Modules": 1441,
#         "go_packagemanager.gpm": 1442,
#         "go_packagemanager.Other": 1443,
#         "go_packagemanager_migrate.No, I don't plan to": 1445,
#         "go_packagemanager_migrate.Yes, planning to adopt / migrate to other package manager(s) - Write in": 1446,
#         "go_packagemanager_migrate.dep": 1447,
#         "go_packagemanager_migrate.godep": 1448,
#         "go_packagemanager_migrate.Go Modules": 1449
#     },
#     "go_packagemanager_migrate": {
#         "go_packagemanager_migrate.No, I don't plan to": 1445,
#         "go_packagemanager_migrate.Yes, planning to adopt / migrate to other package manager(s) - Write in": 1446,
#         "go_packagemanager_migrate.dep": 1447,
#         "go_packagemanager_migrate.godep": 1448,
#         "go_packagemanager_migrate.Go Modules": 1449
#     },
#     "go_frameworks": {
#         "go_frameworks.None": 1450,
#         "go_frameworks.Buffalo": 1451,
#         "go_frameworks.Gin": 1452,
#         "go_frameworks.Macaron": 1453,
#         "go_frameworks.Echo": 1454,
#         "go_frameworks.Beego": 1455,
#         "go_frameworks.Revel": 1456,
#         "go_frameworks.Other": 1457
#     },
#     "go_router": {
#         "go_router.None": 1458,
#         "go_router.standard library": 1459,
#         "go_router.gorilla / mux": 1460,
#         "go_router.go-chi / chi": 1461,
#         "go_router.julienschmidt / httproute": 1462,
#         "go_router.gocraft / web": 1463,
#         "go_router.Other": 1464
#     },
#     "go_testing": {
#         "go_testing.None": 1465,
#         "go_testing.built-in testing": 1466,
#         "go_testing.gocheck": 1467,
#         "go_testing.testify": 1468,
#         "go_testing.ginkgo": 1469,
#         "go_testing.gomega": 1470,
#         "go_testing.goconvey": 1471,
#         "go_testing.gomock": 1472,
#         "go_testing.go-sqlmock": 1473,
#         "go_testing.httpexpect": 1474,
#         "go_testing.Other": 1475
#     },
#     "go_external_deps": {
#         "go_external_deps": 1476
#     },
#     "go_code_size": {
#         "go_code_size": 1477
#     },
#     "primary_proglang": {
#         "primary_proglang.Java": 134,
#         "primary_proglang.C": 135,
#         "primary_proglang.C++": 136,
#         "primary_proglang.Python": 137,
#         "primary_proglang.C#": 138,
#         "primary_proglang.PHP": 139,
#         "primary_proglang.JavaScript": 140,
#         "primary_proglang.Ruby": 141,
#         "primary_proglang.Kotlin": 142,
#         "primary_proglang.Swift": 143,
#         "primary_proglang.Objective-C": 144,
#         "primary_proglang.Scala": 145,
#         "primary_proglang.Go": 146,
#         "primary_proglang.SQL(PL/SQL, T-SQL and otherprogramming extensions over SQL)": 147,
#         "primary_proglang.Rust": 148,
#         "primary_proglang.Haskell": 149,
#         "primary_proglang.HTML / CSS": 150,
#         "primary_proglang.Elixir": 151,
#         "primary_proglang.Crystal": 152,
#         "primary_proglang.Visual Basic": 153,
#         "primary_proglang.R": 154,
#         "primary_proglang.TypeScript": 155,
#         "primary_proglang.Dart": 156,
#         "primary_proglang.CoffeeScript": 157,
#         "primary_proglang.Clojure / ClojureScript": 158,
#         "primary_proglang.Delphi": 159,
#         "primary_proglang.Cobol": 160,
#         "primary_proglang.Groovy": 161,
#         "primary_proglang.Perl": 162,
#         "primary_proglang.Assembly": 163,
#         "primary_proglang.Matlab": 164,
#         "primary_proglang.Lua": 165,
#         "primary_proglang.Shell scripting languages(bash/shell/powershell)": 166,
#         "primary_proglang.Julia": 167,
#         "primary_proglang.F#": 168,
#         "primary_proglang.Other": 169
#     },
#     "kotlin_languages_before": {
#         "kotlin_languages_before.Java": 1041,
#         "kotlin_languages_before.JavaScript/TypeScript": 1042,
#         "kotlin_languages_before.C/C++": 1043,
#         "kotlin_languages_before.C#": 1044,
#         "kotlin_languages_before.PHP": 1045,
#         "kotlin_languages_before.Ruby": 1046,
#         "kotlin_languages_before.Scala": 1047,
#         "kotlin_languages_before.Go": 1048,
#         "kotlin_languages_before.Groovy": 1049,
#         "kotlin_languages_before.Python": 1050,
#         "kotlin_languages_before.Swift": 1051,
#         "kotlin_languages_before.Other": 1052
#     },
#     "devops_server_templating": {
#         "devops_server_templating.None": 1492,
#         "devops_server_templating.Docker": 1493,
#         "devops_server_templating.Vagrant": 1494,
#         "devops_server_templating.Packer": 1495,
#         "devops_server_templating.CoreOS rkt": 1496,
#         "devops_server_templating.Other": 1497
#     },
#     "devops_use_compose": {
#         "devops_use_compose": 1508
#     },
#     "devops_container_orchestration": {
#         "devops_container_orchestration.None": 1509,
#         "devops_container_orchestration.Amazon ECS / Fargate": 1510,
#         "devops_container_orchestration.Amazon EKS": 1511,
#         "devops_container_orchestration.Mesos or DC / OS": 1512,
#         "devops_container_orchestration.Kubernetes (self-managed or fully managed)": 1513,
#         "devops_container_orchestration.Hashicorp Nomad": 1514,
#         "devops_container_orchestration.Docker Swarm": 1515,
#         "devops_container_orchestration.CoreOS Tectonic": 1516,
#         "devops_container_orchestration.Other": 1517
#     },
#     "devops_deploy_docker_repo": {
#         "devops_deploy_docker_repo.I do not deploy": 1521,
#         "devops_deploy_docker_repo.I use only the command line": 1522,
#         "devops_deploy_docker_repo.I use a configuration management tool (Chef, Puppet, Ansible, etc_)": 1523,
#         "devops_deploy_docker_repo.I deploy from CI / CD": 1524,
#         "devops_deploy_docker_repo.I deploy with custom / in-house tools": 1525,
#         "devops_deploy_docker_repo.Other": 1526
#     },
#     "devops_keep_artifacts": {
#         "devops_keep_artifacts.I don't keep artifacts": 1527,
#         "devops_keep_artifacts.Pulp": 1528,
#         "devops_keep_artifacts.Amazon S3": 1529,
#         "devops_keep_artifacts.Archiva": 1530,
#         "devops_keep_artifacts.NuGet": 1531,
#         "devops_keep_artifacts.Nexus": 1532,
#         "devops_keep_artifacts.JFrog Artifactory": 1533,
#         "devops_keep_artifacts.MyGet": 1534,
#         "devops_keep_artifacts.npm": 1535,
#         "devops_keep_artifacts.Docker Hub (private or public)": 1536,
#         "devops_keep_artifacts.Custom tool": 1537,
#         "devops_keep_artifacts.Other": 1538
#     },
#     "accounts": {
#         "accounts.None of the above": 1587,
#         "accounts.Facebook": 1588,
#         "accounts.Twitter": 1589,
#         "accounts.LinkedIn": 1590,
#         "accounts.QQ": 1591,
#         "accounts.Qzone": 1592,
#         "accounts.Baidu Tieba": 1593,
#         "accounts.Quora": 1594,
#         "accounts.Zhihu (\u77e5\u4e4e)": 1595,
#         "accounts.XING": 1596,
#         "accounts.Instagram": 1597,
#         "accounts.VKontakte": 1598,
#         "accounts.GitHub": 1599,
#         "accounts.StackOverflow": 1600,
#         "accounts.Reddit": 1601,
#         "accounts.Other": 1602
#     },
#     "learn_pl": {
#         "learn_pl.I am not learning any programming languages": 1617,
#         "learn_pl.Java": 1618,
#         "learn_pl.\u0421": 1619,
#         "learn_pl.C++": 1620,
#         "learn_pl.Python": 1621,
#         "learn_pl.C#": 1622,
#         "learn_pl.PHP": 1623,
#         "learn_pl.JavaScript": 1624,
#         "learn_pl.Ruby": 1625,
#         "learn_pl.Kotlin": 1626,
#         "learn_pl.Swift": 1627,
#         "learn_pl.Scala": 1628,
#         "learn_pl.Go": 1629,
#         "learn_pl.R": 1630,
#         "learn_pl.TypeScript": 1631,
#         "learn_pl.Haskell": 1632,
#         "learn_pl.Elixir": 1633,
#         "learn_pl.Clojure": 1634,
#         "learn_pl.Rust": 1635,
#         "learn_pl.Other": 1636
#     },
#     "learn_what": {
#         "learn_what.I did not learn any new tools / technologies / programming languages in the last 12 months": 1637,
#         "learn_what.Offline educational organizations": 1638,
#         "learn_what.Books": 1639,
#         "learn_what.Personal teacher/consultant": 1640,
#         "learn_what.Online coding schools": 1641,
#         "learn_what.MOOCs (Coursera, edX, Udacity, etc_)": 1642,
#         "learn_what.Blogs/forums": 1643,
#         "learn_what.Documentation & APIs": 1644,
#         "learn_what.Other": 1645
#     },
#     "ide_theme": {
#         "ide_theme": 525
#     },
#     "salary": {
#         "salary": 1728
#     },
#     "it_core": {
#         "it_core": 1657
#     },
#     "sectors_it": {
#         "sectors_it.Telecom": 1658,
#         "sectors_it.Game development (including mobile games)": 1659,
#         "sectors_it.Mobile development": 1660,
#         "sectors_it.IoT / embedded": 1661,
#         "sectors_it.IT services": 1662,
#         "sectors_it.Cloud computing / platform": 1663,
#         "sectors_it.Big Data / Data analysis": 1664,
#         "sectors_it.Hardware": 1665,
#         "sectors_it.Data center services": 1666,
#         "sectors_it.Software development tools": 1667,
#         "sectors_it.Internet / Search engines": 1668,
#         "sectors_it.Semiconductors": 1669,
#         "sectors_it.E-learning": 1670,
#         "sectors_it.FinTech": 1671,
#         "sectors_it.Healthcare IT": 1672,
#         "sectors_it.Cybersecurity": 1673,
#         "sectors_it.BPO services": 1674,
#         "sectors_it.Other Software (all other types of software)": 1675,
#         "sectors_it.Other": 1676
#     },
#     "sectors_nonit": {
#         "sectors_nonit.Government and defense": 1677,
#         "sectors_nonit.Administration / Management / Business Development": 1678,
#         "sectors_nonit.Banking / Real Estate / Mortgage Financing / Accounting / Finance / Insurance": 1679,
#         "sectors_nonit.Business / Strategic Management": 1680,
#         "sectors_nonit.Construction / Architecture": 1681,
#         "sectors_nonit.Customer Support": 1682,
#         "sectors_nonit.Design": 1683,
#         "sectors_nonit.Education / Training": 1684,
#         "sectors_nonit.Human Resources": 1685,
#         "sectors_nonit.Law": 1686,
#         "sectors_nonit.Logistics/ Transportation": 1687,
#         "sectors_nonit.Machinery": 1688,
#         "sectors_nonit.Aerospace": 1689,
#         "sectors_nonit.Automotive and boating": 1690,
#         "sectors_nonit.Manufacturing": 1691,
#         "sectors_nonit.Marketing": 1692,
#         "sectors_nonit.Medicine / Health": 1693,
#         "sectors_nonit.Non-profit": 1694,
#         "sectors_nonit.Entertainment / Mass media and information / Publishing": 1695,
#         "sectors_nonit.Restaurants / Hospitality / Tourism": 1696,
#         "sectors_nonit.Sales / Distribution / Retail": 1697,
#         "sectors_nonit.Food / Agriculture": 1698,
#         "sectors_nonit.Science": 1699,
#         "sectors_nonit.Security": 1700,
#         "sectors_nonit.Service / Maintenance": 1701,
#         "sectors_nonit.Energy": 1702,
#         "sectors_nonit.Other": 1703
#     },
#     "pair_programming": {
#         "pair_programming": 1720
#     },
#     "devops_infr_provisioning": {
#         "devops_infr_provisioning.None": 1498,
#         "devops_infr_provisioning.Terraform": 1499,
#         "devops_infr_provisioning.CloudFormation": 1500,
#         "devops_infr_provisioning.TOSCA/Cloudify": 1501,
#         "devops_infr_provisioning.OpenStack Heat": 1502,
#         "devops_infr_provisioning.Other": 1503
#     },
#     "devops_involved": {
#         "devops_involved": 1484
#     },
#     "devops_deploy_cloud": {
#         "devops_deploy_cloud.Run scripts on your local workstation / VM": 1543,
#         "devops_deploy_cloud.Use Continuous Integration / Continuous Delivery": 1544,
#         "devops_deploy_cloud.Use your cloud provider's web interface": 1545,
#         "devops_deploy_cloud.Other": 1546
#     },
#     "kind_of_dev": {
#         "kind_of_dev.Product development": 1704,
#         "kind_of_dev.Outsourcing": 1705,
#         "kind_of_dev.Custom-tailored software / websites / applications": 1706,
#         "kind_of_dev.In-house development": 1707,
#         "kind_of_dev.Internal deployment and maintenance of third-party tools": 1708,
#         "kind_of_dev.Customer services development (websites, mobile apps, etc_)": 1709,
#         "kind_of_dev.Open source projects": 1710,
#         "kind_of_dev.Other": 1711
#     },
#     "java_unittesting": {
#         "java_unittesting.JUnit": 555,
#         "java_unittesting.TestNG": 556,
#         "java_unittesting.Mockito": 557,
#         "java_unittesting.PowerMock": 558,
#         "java_unittesting.Spock": 559,
#         "java_unittesting.EasyMock": 560,
#         "java_unittesting.JMockit": 561,
#         "java_unittesting.Other": 562
#     },
#     "swiftoc_platforms": {
#         "swiftoc_platforms.iOS": 1101,
#         "swiftoc_platforms.tvOS": 1102,
#         "swiftoc_platforms.watchOS": 1103,
#         "swiftoc_platforms.macOS": 1104,
#         "swiftoc_platforms.I don\u2019t develop for Apple platforms": 1105
#     },
#     "swiftoc_cpp_libs": {
#         "swiftoc_cpp_libs": 1107
#     },
#     "swiftoc_ui_frameworks": {
#         "swiftoc_ui_frameworks.None": 1123,
#         "swiftoc_ui_frameworks.XCTest": 1124,
#         "swiftoc_ui_frameworks.KIF": 1125,
#         "swiftoc_ui_frameworks.EarlGrey": 1126,
#         "swiftoc_ui_frameworks.iOSSnapshotTestCase (FBSnapshotTestCase)": 1127,
#         "swiftoc_ui_frameworks.Other": 1128
#     },
#     "swiftoc_db_viewer_do": {
#         "swiftoc_db_viewer_do": 1141
#     },
#     "swiftoc_db_viewer": {
#         "swiftoc_db_viewer_do": 1141,
#         "swiftoc_db_viewer": 1142
#     },
#     "swiftoc_together": {
#         "swiftoc_together": 1106
#     },
#     "employment_status": {
#         "employment_status": 0
#     },
#     "test_types": {
#         "test_types.None": 244,
#         "test_types.Unit": 245,
#         "test_types.Integration": 246,
#         "test_types.End-to-End": 247,
#         "test_types.Other": 248
#     },
#     "db": {
#         "db.None": 251,
#         "db.DB2": 252,
#         "db.MS SQL Server": 253,
#         "db.MySQL": 254,
#         "db.Oracle Database": 255,
#         "db.PostgreSQL": 256,
#         "db.SQLite": 257,
#         "db.Cassandra": 258,
#         "db.Couchbase": 259,
#         "db.HBase": 260,
#         "db.MongoDB": 261,
#         "db.Neo4j": 262,
#         "db.Redis": 263,
#         "db.Amazon Redshift": 264,
#         "db.H2": 265,
#         "db.MariaDB": 266,
#         "db.Exasol": 267,
#         "db.ClickHouse": 268,
#         "db.Other": 269,
#         "db_adopt.No, not planning to adopt / migrate": 270,
#         "db_adopt.Yes, planning to adopt / migrate to other database(s) - Write in": 271,
#         "db_adopt.DB2": 272,
#         "db_adopt.MS SQL Server": 273,
#         "db_adopt.MySQL": 274,
#         "db_adopt.Oracle Database": 275,
#         "db_adopt.PostgreSQL": 276,
#         "db_adopt.SQLite": 277,
#         "db_adopt.Cassandra": 278,
#         "db_adopt.Couchbase": 279,
#         "db_adopt.HBase": 280,
#         "db_adopt.MongoDB": 281,
#         "db_adopt.Neo4j": 282,
#         "db_adopt.Redis": 283,
#         "db_adopt.Amazon Redshift": 284,
#         "db_adopt.H2": 285,
#         "db_adopt.MariaDB": 286,
#         "db_adopt.ClickHouse": 287,
#         "db_adopt.Other": 288
#     },
#     "c_dependencymanager": {
#         "c_dependencymanager.None": 625,
#         "c_dependencymanager.build2": 626,
#         "c_dependencymanager.Conan": 627,
#         "c_dependencymanager.Nuget": 628,
#         "c_dependencymanager.vcpkg": 629,
#         "c_dependencymanager.I rely on a system package manager": 630,
#         "c_dependencymanager.Other": 631
#     },
#     "cpp_dependencymanager": {
#         "cpp_dependencymanager.None": 670,
#         "cpp_dependencymanager.build2": 671,
#         "cpp_dependencymanager.Conan": 672,
#         "cpp_dependencymanager.Hunter": 673,
#         "cpp_dependencymanager.Nuget": 674,
#         "cpp_dependencymanager.vcpkg": 675,
#         "cpp_dependencymanager.I rely on a system package manager": 676,
#         "cpp_dependencymanager.Other": 677
#     },
#     "cpp_guidelines_tools": {
#         "cpp_guidelines_tools.None": 696,
#         "cpp_guidelines_tools.Clang-analyzer / Clang Static Analyzer": 697,
#         "cpp_guidelines_tools.Clang-tidy": 698,
#         "cpp_guidelines_tools.Cppcheck": 699,
#         "cpp_guidelines_tools.Coverity": 700,
#         "cpp_guidelines_tools.Cpplint": 701,
#         "cpp_guidelines_tools.PVS-Studio": 702,
#         "cpp_guidelines_tools.Klocwork": 703,
#         "cpp_guidelines_tools.PC-lint / Flexelint": 704,
#         "cpp_guidelines_tools.Parasoft C/C++test": 705,
#         "cpp_guidelines_tools.QA-C++": 706,
#         "cpp_guidelines_tools.Stack": 707,
#         "cpp_guidelines_tools.Tool provided by my IDE (Visual Studio, ReSharper C++, CLion, etc_)": 708,
#         "cpp_guidelines_tools.Other": 709
#     },
#     "cpp_guidelines_sources": {
#         "cpp_guidelines_sources.None": 710,
#         "cpp_guidelines_sources.Effective C++ series (books by Scott Meyers)": 711,
#         "cpp_guidelines_sources.C++ Core Guidelines \u2013 main project (github_com/isocpp/CppCoreGuidelines)": 712,
#         "cpp_guidelines_sources.Guru of the Week / Exceptional C++ series (blog/books by Herb Sutter)": 713,
#         "cpp_guidelines_sources.C++ Coding Standards (book by Herb Sutter and Andrei Alexandrescu)": 714,
#         "cpp_guidelines_sources.Abseil tips of the week": 715,
#         "cpp_guidelines_sources.Google C++ Style Guide": 716,
#         "cpp_guidelines_sources.CERT C++ Secure Coding Standard (www_securecoding_cert_org)": 717,
#         "cpp_guidelines_sources.Coding Standards (Lockheed Martin)": 718,
#         "cpp_guidelines_sources.High Integrity C++ Coding Standard (Programming Research)": 719,
#         "cpp_guidelines_sources.C++ Core Guidelines \u2013 a company-specific fork/branch augmented with internal rules": 720,
#         "cpp_guidelines_sources.MISRA C++ (MIRA Ltd_)": 721,
#         "cpp_guidelines_sources.Other": 722
#     },
#     "python_ds_libs": {
#         "python_ds_libs.None": 757,
#         "python_ds_libs.NumPy": 758,
#         "python_ds_libs.SciPy": 759,
#         "python_ds_libs.Pandas": 760,
#         "python_ds_libs.Matplotlib": 761,
#         "python_ds_libs.Seaborn": 762,
#         "python_ds_libs.SciKit-Learn": 763,
#         "python_ds_libs.Keras": 764,
#         "python_ds_libs.TensorFlow": 765,
#         "python_ds_libs.Theano": 766,
#         "python_ds_libs.NLTK": 767,
#         "python_ds_libs.Gensim": 768,
#         "python_ds_libs.Other": 769
#     },
#     "python_other_libs": {
#         "python_other_libs.None": 770,
#         "python_other_libs.Requests": 771,
#         "python_other_libs.aiohttp": 772,
#         "python_other_libs.PyQT": 773,
#         "python_other_libs.PyGTK": 774,
#         "python_other_libs.wxPython": 775,
#         "python_other_libs.Pillow": 776,
#         "python_other_libs.Tkinter": 777,
#         "python_other_libs.Pygame": 778,
#         "python_other_libs.Twisted": 779,
#         "python_other_libs.Asyncio": 780,
#         "python_other_libs.Kivy": 781,
#         "python_other_libs.Six": 782,
#         "python_other_libs.Scrapy": 783,
#         "python_other_libs.Other": 784
#     },
#     "python_web_libs": {
#         "python_web_libs.None": 745,
#         "python_web_libs.Django": 746,
#         "python_web_libs.TurboGears": 747,
#         "python_web_libs.web2py": 748,
#         "python_web_libs.Bottle": 749,
#         "python_web_libs.CherryPy\u00a0": 750,
#         "python_web_libs.Flask\u00a0": 751,
#         "python_web_libs.Hug": 752,
#         "python_web_libs.Pyramid\u00a0": 753,
#         "python_web_libs.Tornado": 754,
#         "python_web_libs.Falcon": 755,
#         "python_web_libs.Other": 756
#     },
#     "js_sslang": {
#         "js_sslang.CSS": 1269,
#         "js_sslang.Sass": 1270,
#         "js_sslang.SCSS": 1271,
#         "js_sslang.Less": 1272,
#         "js_sslang.PostCSS": 1273,
#         "js_sslang.CSS-in-JS": 1274,
#         "js_sslang.CSS Modules": 1275,
#         "js_sslang.Stylus": 1276,
#         "js_sslang.Other": 1277
#     },
#     "js_graphql": {
#         "js_graphql": 1278
#     },
#     "js_monorepo": {
#         "js_monorepo": 1279
#     },
#     "learn_time": {
#         "learn_time": 1647
#     },
#     "learn_kind_of_content": {
#         "learn_kind_of_content": 1646
#     },
#     "php_qualitytools": {
#         "php_qualitytools.None": 920,
#         "php_qualitytools.PHP_CodeSniffer": 921,
#         "php_qualitytools.PHP CS Fixer": 922,
#         "php_qualitytools.PHPMD": 923,
#         "php_qualitytools.PHPStan": 924,
#         "php_qualitytools.Psalm": 925,
#         "php_qualitytools.Phan": 926,
#         "php_qualitytools.Other": 927
#     },
#     "php_templateengines": {
#         "php_templateengines.None, I use pure PHP": 928,
#         "php_templateengines.None, I don\u2019t render HTML": 929,
#         "php_templateengines.Twig": 930,
#         "php_templateengines.Blade": 931,
#         "php_templateengines.Smarty": 932,
#         "php_templateengines.Mustache": 933,
#         "php_templateengines.Latte": 934,
#         "php_templateengines.Other": 935
#     },
#     "php_profiler": {
#         "php_profiler.None": 936,
#         "php_profiler.Xdebug Profiler": 937,
#         "php_profiler.XHProf": 938,
#         "php_profiler.Blackfire_io": 939,
#         "php_profiler.APM solutions (New Relic, Tideways, etc_)": 940,
#         "php_profiler.HTTP load testing (ab, siege, etc_)": 941,
#         "php_profiler.Other": 942
#     },
#     "devops_use_docker": {
#         "devops_use_docker.Run dockerized utilities": 1504,
#         "devops_use_docker.Run your application in one container, and backing services (e_g_ database)": 1505,
#         "devops_use_docker.Run multiple application containers (e_g_ microservices)": 1506,
#         "devops_use_docker.Other": 1507
#     },
#     "go_modules_outside": {
#         "go_modules_outside": 1478
#     },
#     "go_migrate": {
#         "go_migrate": 1479
#     },
#     "csharp_vsplugins": {
#         "csharp_vsplugins.None": 828,
#         "csharp_vsplugins.ReSharper": 829,
#         "csharp_vsplugins.ReSharper C++": 830,
#         "csharp_vsplugins.CodeRush": 831,
#         "csharp_vsplugins.Visual Assist": 832,
#         "csharp_vsplugins.Roslynator": 833,
#         "csharp_vsplugins.Other": 834
#     },
#     "csharp_vsedition": {
#         "csharp_vsedition": 851
#     },
#     "csharp_msdn_type": {
#         "csharp_msdn_type": 869
#     },
#     "swiftoc_mock": {
#         "swiftoc_mock.None": 1114,
#         "swiftoc_mock.OCMock": 1115,
#         "swiftoc_mock.OCMockito": 1116,
#         "swiftoc_mock.Expecta": 1117,
#         "swiftoc_mock.OCHamcrest": 1118,
#         "swiftoc_mock.Cuckoo": 1119,
#         "swiftoc_mock.SwiftHamcrest": 1120,
#         "swiftoc_mock.Other": 1121
#     },
#     "kotlin_target": {
#         "kotlin_target.JVM": 943,
#         "kotlin_target.Android": 944,
#         "kotlin_target.Kotlin for JavaScript": 945,
#         "kotlin_target.Native": 946
#     },
#     "kotlin_jdk": {
#         "kotlin_jdk.JDK 6": 947,
#         "kotlin_jdk.JDK 7": 948,
#         "kotlin_jdk.JDK 8": 949,
#         "kotlin_jdk.JDK 9": 950,
#         "kotlin_jdk.JDK 10": 951,
#         "kotlin_jdk.JDK 11": 952,
#         "kotlin_jdk.I don't know": 953
#     },
#     "kotlin_android": {
#         "kotlin_android.4_1 \u2013 4_3_1 \u00a0Jelly Bean": 954,
#         "kotlin_android.4_4 \u2013 4_4_4 \u00a0KitKat \u00a0": 955,
#         "kotlin_android.5_0 \u2013 5_1_1 \u00a0Lollipop": 956,
#         "kotlin_android.6_0 \u2013 6_0_1 \u00a0Marshmallow": 957,
#         "kotlin_android.7_0 \u2013 7_1_2 \u00a0Nougat": 958,
#         "kotlin_android.8_0 \u2013 8_1 \u00a0Oreo": 959,
#         "kotlin_android.9_0 Pie": 960,
#         "kotlin_android.Other": 961
#     },
#     "kotlin_platforms": {
#         "kotlin_platforms.iOS (arm32, arm64, emulator x86_64)": 964,
#         "kotlin_platforms.MacOS (x86_64)": 965,
#         "kotlin_platforms.Android (arm32, arm64)": 966,
#         "kotlin_platforms.Windows (mingw x86_64)": 967,
#         "kotlin_platforms.Linux (x86_64, arm32, MIPS, MIPS little endian)": 968,
#         "kotlin_platforms.Other": 969
#     },
#     "kotlin_purposes": {
#         "kotlin_purposes.For work": 1034,
#         "kotlin_purposes.For personal/side projects\u00a0": 1035,
#         "kotlin_purposes.I occasionally play around with Kotlin (Hobby)": 1036,
#         "kotlin_purposes.Other": 1037
#     },
#     "kotlin_projecttypes": {
#         "kotlin_projecttypes.New projects": 1038,
#         "kotlin_projecttypes.Old projects (migration)": 1039,
#         "kotlin_projecttypes.Other": 1040
#     },
#     "communication_tools": {
#         "communication_tools.Email (Microsoft Mail Server, Gmail, etc_)": 377,
#         "communication_tools.Instant messaging/video calling (Slack, Skype, Hipchat, etc_)": 378,
#         "communication_tools.Video conferencing (Google Meet, Zoom, etc_)": 379,
#         "communication_tools.Calendars (Google Calendar, etc_)": 380,
#         "communication_tools.Corporate portal (MS Sharepoint, Pingboard, etc_)": 381,
#         "communication_tools.Service desk/Help desk (Zendesk, Jira Service Desk, etc_)": 382,
#         "communication_tools.None": 383
#     },
#     "mobile_apps": {
#         "mobile_apps.None": 384,
#         "mobile_apps.Email (Microsoft Mail Server, Gmail, etc_)": 385,
#         "mobile_apps.Instant messaging/video calling (Slack, Skype, Hipchat, etc_)": 386,
#         "mobile_apps.Video conferencing (Google Meet, Zoom, etc_)": 387,
#         "mobile_apps.Calendars (Google Calendar, etc_)": 388,
#         "mobile_apps.Corporate portal (MS Sharepoint, Pingboard, etc_)": 389,
#         "mobile_apps.Service desk/Help desk (Zendesk, Jira Service Desk, etc_)": 390
#     },
#     "corporate_mail_server": {
#         "corporate_mail_server": 391
#     },
#     "corporate_suite": {
#         "corporate_suite.None": 392,
#         "corporate_suite.G Suite (Gmail, Google Drive, Meet, etc_)": 393,
#         "corporate_suite.Office 365 (Outlook, Microsoft Teams, SharePoint, etc)": 394,
#         "corporate_suite.Zoho": 395,
#         "corporate_suite.Other": 396
#     },
#     "email_server": {
#         "email_server": 403
#     },
#     "chat": {
#         "chat.Mattermost": 411,
#         "chat.Telegram": 412,
#         "chat.WhatsApp": 413,
#         "chat.Hipchat/Stride": 414,
#         "chat.Viber": 415,
#         "chat.Slack": 416,
#         "chat.Rocket_Chat": 417,
#         "chat.Zulip": 418,
#         "chat.Skype": 419,
#         "chat.Google Hangouts": 420,
#         "chat.IRC": 421,
#         "chat.Other": 422
#     },
#     "video_calls": {
#         "video_calls.Slack": 423,
#         "video_calls.Skype": 424,
#         "video_calls.Skype for Business, Lync": 425,
#         "video_calls.MS Teams": 426,
#         "video_calls.Google Meet": 427,
#         "video_calls.Polycom": 428,
#         "video_calls.Zoom": 429,
#         "video_calls.Other": 430
#     },
#     "knowledge_base": {
#         "knowledge_base.None": 431,
#         "knowledge_base.Confluence": 432,
#         "knowledge_base.MediaWiki": 433,
#         "knowledge_base.GitHub Wiki": 434,
#         "knowledge_base.Stack Overflow for Teams": 435,
#         "knowledge_base.Custom": 436,
#         "knowledge_base.Other": 437
#     },
#     "document_collaboration_platforms": {
#         "document_collaboration_platforms.None": 446,
#         "document_collaboration_platforms.Office 365": 447,
#         "document_collaboration_platforms.Zoho Office Suite": 448,
#         "document_collaboration_platforms. Confluence": 449,
#         "document_collaboration_platforms.Google Docs\u00a0": 450,
#         "document_collaboration_platforms.Dropbox Paper": 451,
#         "document_collaboration_platforms.Quip": 452,
#         "document_collaboration_platforms.Other": 453
#     },
#     "file_sharing_tools": {
#         "file_sharing_tools.None": 438,
#         "file_sharing_tools.Google Drive": 439,
#         "file_sharing_tools.Dropbox": 440,
#         "file_sharing_tools.OneCloud": 441,
#         "file_sharing_tools.Microsoft OneDrive": 442,
#         "file_sharing_tools.Sharepoint": 443,
#         "file_sharing_tools.On premise FTP server": 444,
#         "file_sharing_tools.Other": 445
#     },
#     "swiftoc_serverside": {
#         "swiftoc_serverside": 1150,
#         "swiftoc_serverside_frameworks.Kitura": 1151,
#         "swiftoc_serverside_frameworks.Vapor": 1152,
#         "swiftoc_serverside_frameworks.Perfect": 1153,
#         "swiftoc_serverside_frameworks.Other": 1154
#     },
#     "swiftoc_serverside_frameworks": {
#         "swiftoc_serverside_frameworks.Kitura": 1151,
#         "swiftoc_serverside_frameworks.Vapor": 1152,
#         "swiftoc_serverside_frameworks.Perfect": 1153,
#         "swiftoc_serverside_frameworks.Other": 1154
#     },
#     "rust_how": {
#         "rust_how.Work": 1280,
#         "rust_how.Personal / side projects": 1281,
#         "rust_how.Hobby": 1282,
#         "rust_how.Other": 1283,
#         "rust_how_long": 1284
#     },
#     "rust_how_long": {
#         "rust_how_long": 1284
#     },
#     "rust_version": {
#         "rust_version.Current stable release": 1285,
#         "rust_version.Previous stable release": 1286,
#         "rust_version.Beta release": 1287,
#         "rust_version.Nightly": 1288,
#         "rust_version.1_30 or older": 1289
#     },
#     "rust_other_langs": {
#         "rust_other_langs.None": 1290,
#         "rust_other_langs.C": 1291,
#         "rust_other_langs.C++": 1292,
#         "rust_other_langs.Python": 1293,
#         "rust_other_langs.Java": 1294,
#         "rust_other_langs.Go": 1295,
#         "rust_other_langs.JavaScript": 1296,
#         "rust_other_langs.Other": 1297
#     },
#     "rust_code_interact": {
#         "rust_code_interact.Language interop (foreign functions)": 1298,
#         "rust_code_interact.RPC": 1299,
#         "rust_code_interact.REST API": 1300,
#         "rust_code_interact.Other": 1301
#     },
#     "rust_ide": {
#         "rust_ide.Atom": 1304,
#         "rust_ide.Emacs": 1305,
#         "rust_ide.IntelliJ IDEA": 1306,
#         "rust_ide.CLion": 1307,
#         "rust_ide.Sublime Text": 1308,
#         "rust_ide.Vim": 1309,
#         "rust_ide.VSCode (Visual Studio Code)": 1310,
#         "rust_ide.Other": 1311,
#         "rust_ide_mostlove.Speed/performance": 1313,
#         "rust_ide_mostlove.Ease of use": 1314,
#         "rust_ide_mostlove.Code completion": 1315,
#         "rust_ide_mostlove.Code navigation": 1316,
#         "rust_ide_mostlove.Error highlighting": 1317,
#         "rust_ide_mostlove.Tools integration": 1318,
#         "rust_ide_mostlove.Debugger support": 1319,
#         "rust_ide_mostlove.Other": 1320,
#         "rust_ide_lack.Speed/performance": 1321,
#         "rust_ide_lack.Ease of use": 1322,
#         "rust_ide_lack.Code completion": 1323,
#         "rust_ide_lack.Code navigation": 1324,
#         "rust_ide_lack.Error highlighting": 1325,
#         "rust_ide_lack.Tools integration": 1326,
#         "rust_ide_lack.Debugger support": 1327,
#         "rust_ide_lack.Other": 1328
#     },
#     "rust_build_tool": {
#         "rust_build_tool.Cargo": 1329,
#         "rust_build_tool.Other": 1330
#     },
#     "rust_testing": {
#         "rust_testing.I don\u2019t use testing frameworks": 1331,
#         "rust_testing.Rust tests": 1332,
#         "rust_testing.Other": 1333
#     },
#     "rust_code_coverage": {
#         "rust_code_coverage.I don\u2019t use code coverage tools": 1334,
#         "rust_code_coverage.codecov": 1335,
#         "rust_code_coverage.Other": 1336
#     },
#     "rust_profiler": {
#         "rust_profiler.I don\u2019t use profiling tools": 1337,
#         "rust_profiler.perf": 1338,
#         "rust_profiler.callgrind/cachegrind": 1339,
#         "rust_profiler.Other": 1340
#     },
#     "ai_replace": {
#         "ai_replace": 526
#     },
#     "rust_os": {
#         "rust_os": 1302
#     },
#     "rust_platforms": {
#         "rust_platforms.Linux": 1353,
#         "rust_platforms.Windows": 1354,
#         "rust_platforms.macOS": 1355,
#         "rust_platforms.Android": 1356,
#         "rust_platforms.iOS": 1357,
#         "rust_platforms.WebAssembly": 1358,
#         "rust_platforms.Embedded": 1359
#     },
#     "rust_code_size": {
#         "rust_code_size": 1360
#     },
#     "rust_external_deps": {
#         "rust_external_deps": 1361
#     },
#     "rust_current_codebase": {
#         "rust_current_codebase": 1362
#     },
#     "rust_devs_count": {
#         "rust_devs_count": 1363
#     },
#     "cats_dogs": {
#         "cats_dogs": 1648
#     },
#     "where_survey": {
#         "where_survey": 1584
#     },
#     "rust_primary_ide": {
#         "rust_primary_ide": 1312
#     },
#     "rust_ide_mostlove": {
#         "rust_ide_mostlove.Speed/performance": 1313,
#         "rust_ide_mostlove.Ease of use": 1314,
#         "rust_ide_mostlove.Code completion": 1315,
#         "rust_ide_mostlove.Code navigation": 1316,
#         "rust_ide_mostlove.Error highlighting": 1317,
#         "rust_ide_mostlove.Tools integration": 1318,
#         "rust_ide_mostlove.Debugger support": 1319,
#         "rust_ide_mostlove.Other": 1320
#     },
#     "rust_ide_lack": {
#         "rust_ide_lack.Speed/performance": 1321,
#         "rust_ide_lack.Ease of use": 1322,
#         "rust_ide_lack.Code completion": 1323,
#         "rust_ide_lack.Code navigation": 1324,
#         "rust_ide_lack.Error highlighting": 1325,
#         "rust_ide_lack.Tools integration": 1326,
#         "rust_ide_lack.Debugger support": 1327,
#         "rust_ide_lack.Other": 1328
#     },
#     "calendar_software": {
#         "calendar_software.Google Calendar": 404,
#         "calendar_software.Outlook": 405,
#         "calendar_software.iCal (Calendar App in Mac)": 406,
#         "calendar_software.Microsoft Exchange": 407,
#         "calendar_software.IBM Domino": 408,
#         "calendar_software.Fantastical": 409,
#         "calendar_software.Other": 410
#     },
#     "email_clients": {
#         "email_clients.Gmail": 397,
#         "email_clients.Yahoo": 398,
#         "email_clients.Outlook": 399,
#         "email_clients.Thunderbird": 400,
#         "email_clients.Mail in macOS": 401,
#         "email_clients.Other": 402
#     },
#     "code_in_dreams": {
#         "code_in_dreams": 1483
#     },
#     "where_host": {
#         "where_host.Locally (on your workstation, developer environment or device)": 1539,
#         "where_host.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1540,
#         "where_host.Cloud Service (AWS, MS Azure, GCP, etc_)": 1541,
#         "where_host.Other": 1542,
#         "where_host_primarly": 1547,
#         "where_host_plan.Locally (on your workstation, developer environment or device)": 1557,
#         "where_host_plan.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1558,
#         "where_host_plan.Amazon Web Services": 1559,
#         "where_host_plan.Microsoft Azure": 1560,
#         "where_host_plan.Google Cloud Platform": 1561,
#         "where_host_plan.Rackspace": 1562,
#         "where_host_plan.RedHat OpenShift": 1563,
#         "where_host_plan.IBM SoftLayer": 1564,
#         "where_host_plan.Cloud Foundry": 1565,
#         "where_host_plan.Heroku": 1566,
#         "where_host_plan.Other": 1567
#     },
#     "where_host_primarly": {
#         "where_host_primarly": 1547
#     },
#     "where_host_plan": {
#         "where_host_plan.Locally (on your workstation, developer environment or device)": 1557,
#         "where_host_plan.Private Servers (hosted on your company\u2019s cluster or server on-premises)": 1558,
#         "where_host_plan.Amazon Web Services": 1559,
#         "where_host_plan.Microsoft Azure": 1560,
#         "where_host_plan.Google Cloud Platform": 1561,
#         "where_host_plan.Rackspace": 1562,
#         "where_host_plan.RedHat OpenShift": 1563,
#         "where_host_plan.IBM SoftLayer": 1564,
#         "where_host_plan.Cloud Foundry": 1565,
#         "where_host_plan.Heroku": 1566,
#         "where_host_plan.Other": 1567
#     },
#     "rust_projecttypes": {
#         "rust_projecttypes.Web development": 1341,
#         "rust_projecttypes.Systems programming": 1342,
#         "rust_projecttypes.DevOps": 1343,
#         "rust_projecttypes.Network programming": 1344,
#         "rust_projecttypes.Databases": 1345,
#         "rust_projecttypes.Security": 1346,
#         "rust_projecttypes.Desktop / GUI applications": 1347,
#         "rust_projecttypes.Embedded devices / Internet of Things": 1348,
#         "rust_projecttypes.Academic / Scientific / Numeric": 1349,
#         "rust_projecttypes.Machine learning / Artificial intelligence": 1350,
#         "rust_projecttypes.Games": 1351,
#         "rust_projecttypes.Other": 1352
#     },
#     "commute": {
#         "commute.I work / study from home": 1603,
#         "commute.Car": 1604,
#         "commute.Public transport": 1605,
#         "commute.Bike": 1606,
#         "commute.Motorcycle": 1607,
#         "commute.By foot": 1608,
#         "commute.Other": 1609
#     },
#     "fuel": {
#         "fuel": 1610
#     },
#     "go_how": {
#         "go_how": 1426
#     },
#     "sql_oracle": {
#         "sql_oracle.18c": 1373,
#         "sql_oracle.12_x": 1374,
#         "sql_oracle.11_x": 1375,
#         "sql_oracle.10_x": 1376,
#         "sql_oracle.9_x": 1377,
#         "sql_oracle.I'm not sure": 1378,
#         "sql_oracle.Other": 1379
#     },
#     "kotlin_server_client": {
#         "kotlin_server_client.Server-side (like Node_js)": 962,
#         "kotlin_server_client.Browser": 963
#     },
#     "go_templateengines": {
#         "go_templateengines.None": 1430,
#         "go_templateengines.text/template": 1431,
#         "go_templateengines.html/template": 1432,
#         "go_templateengines.Plush": 1433,
#         "go_templateengines.Pongo2": 1434,
#         "go_templateengines.Other": 1435
#     },
#     "go_ide": {
#         "go_ide": 1444
#     },
#     "position_level": {
#         "position_level": 18
#     },
#     "do_crossplatform": {
#         "do_crossplatform": 53
#     },
#     "crossplatform_platform": {
#         "crossplatform_platform.Windows": 54,
#         "crossplatform_platform.Unix/Linux": 55,
#         "crossplatform_platform.macOS": 56,
#         "crossplatform_platform.iOS": 57,
#         "crossplatform_platform.Android": 58,
#         "crossplatform_platform.Web": 59,
#         "crossplatform_platform.Embedded": 60,
#         "crossplatform_platform.Other": 61
#     },
#     "crossplatform_how_os": {
#         "crossplatform_how_os.Using containers (e_g_ Docker, Vagrant)": 62,
#         "crossplatform_how_os.Using VMs (e_g_ VirtualBox, vSphere)": 63,
#         "crossplatform_how_os.Using physical machines/devices": 64,
#         "crossplatform_how_os.I don\u2019t normally work with different OSes/platforms": 65,
#         "crossplatform_how_os.Other": 66
#     },
#     "crossplatform_how_fs": {
#         "crossplatform_how_fs.Using OS file browser (e_g_ File Explorer, Files, Finder)": 67,
#         "crossplatform_how_fs.Using the IDE": 68,
#         "crossplatform_how_fs.Using terminal (e_g_ cd, dir/ls, copy, mv)": 69,
#         "crossplatform_how_fs.Using third-party GUI file managers (e_g_ muCommander, Path Finder, Total Commander)": 70,
#         "crossplatform_how_fs.Using third-party terminal-based file managers (e_g_ Midnight Commander, Far Manager)": 71
#     },
#     "remote_files_operations": {
#         "remote_files_operations.Browse files": 72,
#         "remote_files_operations.Copy/move/delete files": 73,
#         "remote_files_operations.Edit files": 74,
#         "remote_files_operations.I don\u2019t normally work with remote files": 75
#     },
#     "vcs_how": {
#         "vcs_how.From terminal": 514,
#         "vcs_how.Using specialized tools (e_g_ GitKraken, Sourcetree, GitHub desktop, etc_)": 515,
#         "vcs_how.From IDE": 516,
#         "vcs_how.From web browser": 517,
#         "vcs_how.Other": 518
#     },
#     "is_testing_integral": {
#         "is_testing_integral": 289
#     },
#     "do_case_design": {
#         "do_case_design": 290
#     },
#     "test_design_how": {
#         "test_design_how": 291
#     },
#     "testing_types": {
#         "testing_types.None": 292,
#         "testing_types.Regression testing": 293,
#         "testing_types.Functional testing": 294,
#         "testing_types.Security testing": 295,
#         "testing_types.Usability testing": 296,
#         "testing_types.Performance testing": 297,
#         "testing_types.Stress testing": 298,
#         "testing_types.Stability testing": 299,
#         "testing_types.Smoke testing": 300,
#         "testing_types.I\u2019m not sure": 301,
#         "testing_types.Other": 302
#     },
#     "testers_qa_ratio": {
#         "testers_qa_ratio": 303
#     },
#     "store_testcases": {
#         "store_testcases.I don\u2019t use any specific tools_": 306,
#         "store_testcases.Microsoft Office documents (such as Excel spreadsheets)": 307,
#         "store_testcases.Special test case management tools": 308,
#         "store_testcases.Other": 309
#     },
#     "automated_tests": {
#         "automated_tests": 310
#     },
#     "auto_tests_pl": {
#         "auto_tests_pl.None": 334,
#         "auto_tests_pl.Python": 335,
#         "auto_tests_pl.JavaScript": 336,
#         "auto_tests_pl.Java": 337,
#         "auto_tests_pl.Kotlin": 338,
#         "auto_tests_pl.C#": 339,
#         "auto_tests_pl.Ruby": 340,
#         "auto_tests_pl.Other": 341
#     },
#     "testers_qa_pskills": {
#         "testers_qa_pskills": 304
#     },
#     "testers_qa_manual": {
#         "testers_qa_manual": 305
#     },
#     "auto_tests_frameworks": {
#         "auto_tests_frameworks.None": 311,
#         "auto_tests_frameworks.TestNG": 312,
#         "auto_tests_frameworks.JUnit": 313,
#         "auto_tests_frameworks.NUnit / xUnit_Net": 314,
#         "auto_tests_frameworks.MSTest / VSTest": 315,
#         "auto_tests_frameworks.Robot Framework": 316,
#         "auto_tests_frameworks.Cucumber": 317,
#         "auto_tests_frameworks.SpecFlow": 318,
#         "auto_tests_frameworks.RSpec": 319,
#         "auto_tests_frameworks.Selenium WebDriver": 320,
#         "auto_tests_frameworks.Allure": 321,
#         "auto_tests_frameworks.Other": 322
#     },
#     "auto_tests_tools": {
#         "auto_tests_tools.None": 323,
#         "auto_tests_tools.SoapUI": 324,
#         "auto_tests_tools.Apache JMeter": 325,
#         "auto_tests_tools.Katalon Studio": 326,
#         "auto_tests_tools.Postman": 327,
#         "auto_tests_tools.Other": 328
#     },
#     "testing_platforms": {
#         "testing_platforms.None": 329,
#         "testing_platforms.SauceLabs": 330,
#         "testing_platforms.BrowserStack": 331,
#         "testing_platforms.CrossBrowserTesting": 332,
#         "testing_platforms.Other": 333
#     },
#     "go_buildsystem": {
#         "go_buildsystem.Go build": 1480,
#         "go_buildsystem.Bazel": 1481,
#         "go_buildsystem.Other": 1482
#     },
#     "devops_run_cont_apps": {
#         "devops_run_cont_apps.Docker Compose": 1518,
#         "devops_run_cont_apps.Minikube": 1519,
#         "devops_run_cont_apps.Other": 1520
#     },
#     "kotlin_app_types": {
#         "kotlin_app_types.Web Back-end": 970,
#         "kotlin_app_types.Web Front-end": 971,
#         "kotlin_app_types.Mobile": 972,
#         "kotlin_app_types.Desktop": 973,
#         "kotlin_app_types.Data analysis / BI": 974,
#         "kotlin_app_types.Machine Learning": 975,
#         "kotlin_app_types.Game development": 976,
#         "kotlin_app_types.IoT": 977,
#         "kotlin_app_types.Embedded": 978,
#         "kotlin_app_types.Library or framework": 979,
#         "kotlin_app_types.Tooling": 980,
#         "kotlin_app_types.Other": 981
#     },
#     "kotlin_jb_libs": {
#         "kotlin_jb_libs.None": 982,
#         "kotlin_jb_libs.kotlin-wrappers/kotlin-react": 983,
#         "kotlin_jb_libs.kotlin-wrappers/kotlin-css": 984,
#         "kotlin_jb_libs.kotlin-wrappers/*": 985,
#         "kotlin_jb_libs.kotlinx_coroutines": 986,
#         "kotlin_jb_libs.kotlinx_html": 987,
#         "kotlin_jb_libs.kotlinx_dom": 988,
#         "kotlin_jb_libs.kotlinx_reflect_lite": 989,
#         "kotlin_jb_libs.Anko Commons": 990,
#         "kotlin_jb_libs.Anko Layouts": 991,
#         "kotlin_jb_libs.Anko SQLite": 992,
#         "kotlin_jb_libs.Anko Coroutines": 993,
#         "kotlin_jb_libs.kotlin_test": 994,
#         "kotlin_jb_libs.Ktor": 995,
#         "kotlin_jb_libs.Dokka": 996,
#         "kotlin_jb_libs.Exposed": 997,
#         "kotlin_jb_libs.Other": 998
#     },
#     "kotlin_other_libs": {
#         "kotlin_other_libs.None": 999,
#         "kotlin_other_libs.Kotlin Android Extensions": 1000,
#         "kotlin_other_libs.jackson-module-kotlin": 1001,
#         "kotlin_other_libs.TornadoFX": 1002,
#         "kotlin_other_libs.KotlinTest": 1003,
#         "kotlin_other_libs.detekt": 1004,
#         "kotlin_other_libs.kotlin-logging": 1005,
#         "kotlin_other_libs.RxKotlin": 1006,
#         "kotlin_other_libs.Spek": 1007,
#         "kotlin_other_libs.HamKrest": 1008,
#         "kotlin_other_libs.Kotlin-NoSQL": 1009,
#         "kotlin_other_libs.Fuel": 1010,
#         "kotlin_other_libs.Kotter Knife": 1011,
#         "kotlin_other_libs.Kotson": 1012,
#         "kotlin_other_libs.Kodein": 1013,
#         "kotlin_other_libs.Klaxon": 1014,
#         "kotlin_other_libs.mockito-kotlin": 1015,
#         "kotlin_other_libs.khttp": 1016,
#         "kotlin_other_libs.spark-kotlin": 1017,
#         "kotlin_other_libs.javalin": 1018,
#         "kotlin_other_libs.http4k": 1019,
#         "kotlin_other_libs.Kluent": 1020,
#         "kotlin_other_libs.koin": 1021,
#         "kotlin_other_libs.ktlint": 1022,
#         "kotlin_other_libs.kscript": 1023,
#         "kotlin_other_libs.Spring": 1024,
#         "kotlin_other_libs.Spring Boot": 1025,
#         "kotlin_other_libs.Vert_x for Kotlin": 1026,
#         "kotlin_other_libs.Arrow": 1027,
#         "kotlin_other_libs.RxBinding": 1028,
#         "kotlin_other_libs.Okio": 1029,
#         "kotlin_other_libs.DBFlow": 1030,
#         "kotlin_other_libs.Material Dialogs": 1031,
#         "kotlin_other_libs.Other": 1032
#     },
#     "pull_requests": {
#         "pull_requests": 519
#     }
# }
#
