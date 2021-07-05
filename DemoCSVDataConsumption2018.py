import json

from pyjetbrainsdevecosystem.data_import_utils import unpack_csv_data, split_data_by_dash

questions_dict = {}
with open('survey_data/2018/DevEcosystem 2018 questions_outside.txt',
          encoding='utf8') as questions_text:
    for row in questions_text.readlines():
        question, description = split_data_by_dash(row, 2018)
        questions_dict.update({question: description})

question_column_map = {}
with open('survey_data/2018/sharing_data_outside.csv',
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

# print(json.dumps(question_column_map, indent=4))
# {
#     "employemnt.status": {
#         "employemnt.status": 0
#     },
#     "job.role": {
#         "job.role.Developer / Programmer/ Software Engineer": 1,
#         "job.role.DevOps Engineer / Infrastructure Developer / etc": 2,
#         "job.role.DBA": 3,
#         "job.role.Architect": 4,
#         "job.role.Tester / QA Engineer": 5,
#         "job.role.Technical support": 6,
#         "job.role.Data analyst / Data engineer": 7,
#         "job.role.Business analyst": 8,
#         "job.role.Team Lead": 9,
#         "job.role.Systems analyst": 10,
#         "job.role.Product Manager": 11,
#         "job.role.UX / UI Designer": 12,
#         "job.role.CIO / CEO / CTO": 13,
#         "job.role.Instructor / Teacher / Tutor / etc": 14,
#         "job.role.Other": 15
#     },
#     "dev.environment": {
#         "dev.environment.Windows": 16,
#         "dev.environment.Unix / Linux": 17,
#         "dev.environment.macOS": 18,
#         "dev.environment.Other - Write In": 19
#     },
#     "job.app.type": {
#         "job.app.type.I don't develop anything for money": 20,
#         "job.app.type.Web Back-end": 21,
#         "job.app.type.Web Front-end": 22,
#         "job.app.type.Mobile applications": 23,
#         "job.app.type.Desktop": 24,
#         "job.app.type.Other Back-end": 25,
#         "job.app.type.Data analysis": 26,
#         "job.app.type.BI": 27,
#         "job.app.type.Machine learning": 28,
#         "job.app.type.Libraries / Frameworks": 29,
#         "job.app.type.Embedded / IoT": 30,
#         "job.app.type.Other - Write In": 31
#     },
#     "hobby.app.type": {
#         "hobby.app.type.I don't develop anything for free / only as a hobby": 32,
#         "hobby.app.type.Web Back-end": 33,
#         "hobby.app.type.Web Front-end": 34,
#         "hobby.app.type.Mobile applications": 35,
#         "hobby.app.type.Desktop": 36,
#         "hobby.app.type.Other Back-end": 37,
#         "hobby.app.type.Data analysis": 38,
#         "hobby.app.type.BI": 39,
#         "hobby.app.type.Machine learning": 40,
#         "hobby.app.type.Embedded / IoT": 41,
#         "hobby.app.type.Libraries / Frameworks": 42,
#         "hobby.app.type.Other - Write In": 43
#     },
#     "target.os": {
#         "target.os.Windows": 44
#     },
#     "desktop.os": {
#         "desktop.os.Unix / Linux": 45,
#         "desktop.os.macOS": 46,
#         "desktop.os.Other - Write In": 47
#     },
#     "mobile.os": {
#         "mobile.os.Android": 48,
#         "mobile.os.iOS": 49,
#         "mobile.os.Other - Write In": 50
#     },
#     "mobile.dev.tools": {
#         "mobile.dev.tools.native.tools": 51,
#         "mobile.dev.tools.crossplatform.tools": 52
#     },
#     "programming.language": {
#         "programming.language.Java": 53,
#         "programming.language.C": 54,
#         "programming.language.C++": 55,
#         "programming.language.Python": 56,
#         "programming.language.C#": 57,
#         "programming.language.PHP": 58,
#         "programming.language.JavaScript": 59,
#         "programming.language.Ruby": 60,
#         "programming.language.Elixir": 61,
#         "programming.language.Crystal": 62,
#         "programming.language.Kotlin": 63,
#         "programming.language.Swift": 64,
#         "programming.language.Objective-C": 65,
#         "programming.language.Visual Basic": 66,
#         "programming.language.Scala": 67,
#         "programming.language.Go": 68,
#         "programming.language.HTML / CSS": 69,
#         "programming.language.Haskell": 70,
#         "programming.language.R": 71,
#         "programming.language.SQL": 72,
#         "programming.language.TypeScript": 73,
#         "programming.language.Dart": 74,
#         "programming.language.CoffeeScript": 75,
#         "programming.language.Clojure / ClojureScript": 76,
#         "programming.language.Delphi": 77,
#         "programming.language.Cobol": 78,
#         "programming.language.Groovy": 79,
#         "programming.language.Rust": 80,
#         "programming.language.Ceylon": 81,
#         "programming.language.Perl": 82,
#         "programming.language.Assembly": 83,
#         "programming.language.Matlab": 84,
#         "programming.language.Lua": 85,
#         "programming.language.Shell": 86,
#         "programming.language.Julia": 87,
#         "programming.language.F#": 88,
#         "programming.language.Other": 89,
#         "programming.language.migrate.Java": 90,
#         "programming.language.migrate.C": 91,
#         "programming.language.migrate.C++": 92,
#         "programming.language.migrate.Python": 93,
#         "programming.language.migrate.C#": 94,
#         "programming.language.migrate.PHP": 95,
#         "programming.language.migrate.JavaScript": 96,
#         "programming.language.migrate.Ruby": 97,
#         "programming.language.migrate.Elixir": 98,
#         "programming.language.migrate.Crystal": 99,
#         "programming.language.migrate.Kotlin": 100,
#         "programming.language.migrate.Swift": 101,
#         "programming.language.migrate.Objective-C": 102,
#         "programming.language.migrate.Visual Basic": 103,
#         "programming.language.migrate.Scala": 104,
#         "programming.language.migrate.Go": 105,
#         "programming.language.migrate.HTML / CSS": 106,
#         "programming.language.migrate.Haskell": 107,
#         "programming.language.migrate.R": 108,
#         "programming.language.migrate.SQL": 109,
#         "programming.language.migrate.TypeScript": 110,
#         "programming.language.migrate.Dart": 111,
#         "programming.language.migrate.CoffeeScript": 112,
#         "programming.language.migrate.Clojure / ClojureScript": 113,
#         "programming.language.migrate.Delphi": 114,
#         "programming.language.migrate.Cobol": 115,
#         "programming.language.migrate.Groovy": 116,
#         "programming.language.migrate.Rust": 117,
#         "programming.language.migrate.Ceylon": 118,
#         "programming.language.migrate.Perl": 119,
#         "programming.language.migrate.Assembly": 120,
#         "programming.language.migrate.Matlab": 121,
#         "programming.language.migrate.Lua": 122,
#         "programming.language.migrate.Shell": 123,
#         "programming.language.migrate.Julia": 124,
#         "programming.language.migrate.F#": 125,
#         "programming.language.migrate.Planning to adopt / migrate to other language(s) - Write in": 126,
#         "programming.language.migrate.No, not planning to adopt / migrate": 127,
#         "programming.language.primary.Java": 128,
#         "programming.language.primary.C": 129,
#         "programming.language.primary.C++": 130,
#         "programming.language.primary.Python": 131,
#         "programming.language.primary.C#": 132,
#         "programming.language.primary.PHP": 133,
#         "programming.language.primary.JavaScript": 134,
#         "programming.language.primary.Ruby": 135,
#         "programming.language.primary.Elixir": 136,
#         "programming.language.primary.Crystal": 137,
#         "programming.language.primary.Kotlin": 138,
#         "programming.language.primary.Swift": 139,
#         "programming.language.primary.Objective-C": 140,
#         "programming.language.primary.Visual Basic": 141,
#         "programming.language.primary.Scala": 142,
#         "programming.language.primary.Go": 143,
#         "programming.language.primary.HTML / CSS": 144,
#         "programming.language.primary.Haskell": 145,
#         "programming.language.primary.R": 146,
#         "programming.language.primary.SQL<br />(PL/SQL, T-SQL and other<br />programming extensions over SQL)": 147,
#         "programming.language.primary.TypeScript": 148,
#         "programming.language.primary.Dart": 149,
#         "programming.language.primary.CoffeeScript": 150,
#         "programming.language.primary.Clojure / ClojureScript": 151,
#         "programming.language.primary.Delphi": 152,
#         "programming.language.primary.Cobol": 153,
#         "programming.language.primary.Groovy": 154,
#         "programming.language.primary.Rust": 155,
#         "programming.language.primary.Ceylon": 156,
#         "programming.language.primary.Perl": 157,
#         "programming.language.primary.Assembly": 158,
#         "programming.language.primary.Matlab": 159,
#         "programming.language.primary.Lua": 160,
#         "programming.language.primary.Shell scripting languages<br />(bash/shell/powershell)": 161,
#         "programming.language.primary.Julia": 162,
#         "programming.language.primary.F#": 163,
#         "programming.language.primary.Other - Write In": 164,
#         "programming.language.primary.rank.Java": 165,
#         "programming.language.primary.rank.C": 166,
#         "programming.language.primary.rank.C++": 167,
#         "programming.language.primary.rank.Python": 168,
#         "programming.language.primary.rank.C#": 169,
#         "programming.language.primary.rank.PHP": 170,
#         "programming.language.primary.rank.JavaScript": 171,
#         "programming.language.primary.rank.Ruby": 172,
#         "programming.language.primary.rank.Elixir": 173,
#         "programming.language.primary.rank.Crystal": 174,
#         "programming.language.primary.rank.Kotlin": 175,
#         "programming.language.primary.rank.Swift": 176,
#         "programming.language.primary.rank.Objective-C": 177,
#         "programming.language.primary.rank.Visual Basic": 178,
#         "programming.language.primary.rank.Scala": 179,
#         "programming.language.primary.rank.Go": 180,
#         "programming.language.primary.rank.HTML / CSS": 181,
#         "programming.language.primary.rank.Haskell": 182,
#         "programming.language.primary.rank.R": 183,
#         "programming.language.primary.rank.SQL<br />(PL/SQL, T-SQL and other<br />programming extensions over SQL)": 184,
#         "programming.language.primary.rank.TypeScript": 185,
#         "programming.language.primary.rank.Dart": 186,
#         "programming.language.primary.rank.CoffeeScript": 187,
#         "programming.language.primary.rank.Clojure / ClojureScript": 188,
#         "programming.language.primary.rank.Delphi": 189,
#         "programming.language.primary.rank.Cobol": 190,
#         "programming.language.primary.rank.Groovy": 191,
#         "programming.language.primary.rank.Rust": 192,
#         "programming.language.primary.rank.Ceylon": 193,
#         "programming.language.primary.rank.Perl": 194,
#         "programming.language.primary.rank.Assembly": 195,
#         "programming.language.primary.rank.Matlab": 196,
#         "programming.language.primary.rank.Lua": 197,
#         "programming.language.primary.rank.Shell scripting languages<br />(bash/shell/powershell)": 198,
#         "programming.language.primary.rank.Julia": 199,
#         "programming.language.primary.rank.F#": 200,
#         "programming.languages.learning.I am not learning any programming languages": 1010,
#         "programming.languages.learning.Java": 1011,
#         "programming.languages.learning.C": 1012,
#         "programming.languages.learning.C++": 1013,
#         "programming.languages.learning.Python": 1014,
#         "programming.languages.learning.C#": 1015,
#         "programming.languages.learning.PHP": 1016,
#         "programming.languages.learning.JavaScript": 1017,
#         "programming.languages.learning.Ruby": 1018,
#         "programming.languages.learning.Kotlin": 1019,
#         "programming.languages.learning.Swift": 1020,
#         "programming.languages.learning.Scala": 1021,
#         "programming.languages.learning.Go": 1022,
#         "programming.languages.learning.R": 1023,
#         "programming.languages.learning.TypeScript": 1024,
#         "programming.languages.learning.Rust": 1025,
#         "programming.languages.learning.Other - Write In": 1026
#     },
#     "programming.language.migrate": {
#         "programming.language.migrate.Java": 90,
#         "programming.language.migrate.C": 91,
#         "programming.language.migrate.C++": 92,
#         "programming.language.migrate.Python": 93,
#         "programming.language.migrate.C#": 94,
#         "programming.language.migrate.PHP": 95,
#         "programming.language.migrate.JavaScript": 96,
#         "programming.language.migrate.Ruby": 97,
#         "programming.language.migrate.Elixir": 98,
#         "programming.language.migrate.Crystal": 99,
#         "programming.language.migrate.Kotlin": 100,
#         "programming.language.migrate.Swift": 101,
#         "programming.language.migrate.Objective-C": 102,
#         "programming.language.migrate.Visual Basic": 103,
#         "programming.language.migrate.Scala": 104,
#         "programming.language.migrate.Go": 105,
#         "programming.language.migrate.HTML / CSS": 106,
#         "programming.language.migrate.Haskell": 107,
#         "programming.language.migrate.R": 108,
#         "programming.language.migrate.SQL": 109,
#         "programming.language.migrate.TypeScript": 110,
#         "programming.language.migrate.Dart": 111,
#         "programming.language.migrate.CoffeeScript": 112,
#         "programming.language.migrate.Clojure / ClojureScript": 113,
#         "programming.language.migrate.Delphi": 114,
#         "programming.language.migrate.Cobol": 115,
#         "programming.language.migrate.Groovy": 116,
#         "programming.language.migrate.Rust": 117,
#         "programming.language.migrate.Ceylon": 118,
#         "programming.language.migrate.Perl": 119,
#         "programming.language.migrate.Assembly": 120,
#         "programming.language.migrate.Matlab": 121,
#         "programming.language.migrate.Lua": 122,
#         "programming.language.migrate.Shell": 123,
#         "programming.language.migrate.Julia": 124,
#         "programming.language.migrate.F#": 125,
#         "programming.language.migrate.Planning to adopt / migrate to other language(s) - Write in": 126,
#         "programming.language.migrate.No, not planning to adopt / migrate": 127
#     },
#     "programming.language.primary": {
#         "programming.language.primary.Java": 128,
#         "programming.language.primary.C": 129,
#         "programming.language.primary.C++": 130,
#         "programming.language.primary.Python": 131,
#         "programming.language.primary.C#": 132,
#         "programming.language.primary.PHP": 133,
#         "programming.language.primary.JavaScript": 134,
#         "programming.language.primary.Ruby": 135,
#         "programming.language.primary.Elixir": 136,
#         "programming.language.primary.Crystal": 137,
#         "programming.language.primary.Kotlin": 138,
#         "programming.language.primary.Swift": 139,
#         "programming.language.primary.Objective-C": 140,
#         "programming.language.primary.Visual Basic": 141,
#         "programming.language.primary.Scala": 142,
#         "programming.language.primary.Go": 143,
#         "programming.language.primary.HTML / CSS": 144,
#         "programming.language.primary.Haskell": 145,
#         "programming.language.primary.R": 146,
#         "programming.language.primary.SQL<br />(PL/SQL, T-SQL and other<br />programming extensions over SQL)": 147,
#         "programming.language.primary.TypeScript": 148,
#         "programming.language.primary.Dart": 149,
#         "programming.language.primary.CoffeeScript": 150,
#         "programming.language.primary.Clojure / ClojureScript": 151,
#         "programming.language.primary.Delphi": 152,
#         "programming.language.primary.Cobol": 153,
#         "programming.language.primary.Groovy": 154,
#         "programming.language.primary.Rust": 155,
#         "programming.language.primary.Ceylon": 156,
#         "programming.language.primary.Perl": 157,
#         "programming.language.primary.Assembly": 158,
#         "programming.language.primary.Matlab": 159,
#         "programming.language.primary.Lua": 160,
#         "programming.language.primary.Shell scripting languages<br />(bash/shell/powershell)": 161,
#         "programming.language.primary.Julia": 162,
#         "programming.language.primary.F#": 163,
#         "programming.language.primary.Other - Write In": 164,
#         "programming.language.primary.rank.Java": 165,
#         "programming.language.primary.rank.C": 166,
#         "programming.language.primary.rank.C++": 167,
#         "programming.language.primary.rank.Python": 168,
#         "programming.language.primary.rank.C#": 169,
#         "programming.language.primary.rank.PHP": 170,
#         "programming.language.primary.rank.JavaScript": 171,
#         "programming.language.primary.rank.Ruby": 172,
#         "programming.language.primary.rank.Elixir": 173,
#         "programming.language.primary.rank.Crystal": 174,
#         "programming.language.primary.rank.Kotlin": 175,
#         "programming.language.primary.rank.Swift": 176,
#         "programming.language.primary.rank.Objective-C": 177,
#         "programming.language.primary.rank.Visual Basic": 178,
#         "programming.language.primary.rank.Scala": 179,
#         "programming.language.primary.rank.Go": 180,
#         "programming.language.primary.rank.HTML / CSS": 181,
#         "programming.language.primary.rank.Haskell": 182,
#         "programming.language.primary.rank.R": 183,
#         "programming.language.primary.rank.SQL<br />(PL/SQL, T-SQL and other<br />programming extensions over SQL)": 184,
#         "programming.language.primary.rank.TypeScript": 185,
#         "programming.language.primary.rank.Dart": 186,
#         "programming.language.primary.rank.CoffeeScript": 187,
#         "programming.language.primary.rank.Clojure / ClojureScript": 188,
#         "programming.language.primary.rank.Delphi": 189,
#         "programming.language.primary.rank.Cobol": 190,
#         "programming.language.primary.rank.Groovy": 191,
#         "programming.language.primary.rank.Rust": 192,
#         "programming.language.primary.rank.Ceylon": 193,
#         "programming.language.primary.rank.Perl": 194,
#         "programming.language.primary.rank.Assembly": 195,
#         "programming.language.primary.rank.Matlab": 196,
#         "programming.language.primary.rank.Lua": 197,
#         "programming.language.primary.rank.Shell scripting languages<br />(bash/shell/powershell)": 198,
#         "programming.language.primary.rank.Julia": 199,
#         "programming.language.primary.rank.F#": 200
#     },
#     "programming.language.primary.rank": {
#         "programming.language.primary.rank.Java": 165,
#         "programming.language.primary.rank.C": 166,
#         "programming.language.primary.rank.C++": 167,
#         "programming.language.primary.rank.Python": 168,
#         "programming.language.primary.rank.C#": 169,
#         "programming.language.primary.rank.PHP": 170,
#         "programming.language.primary.rank.JavaScript": 171,
#         "programming.language.primary.rank.Ruby": 172,
#         "programming.language.primary.rank.Elixir": 173,
#         "programming.language.primary.rank.Crystal": 174,
#         "programming.language.primary.rank.Kotlin": 175,
#         "programming.language.primary.rank.Swift": 176,
#         "programming.language.primary.rank.Objective-C": 177,
#         "programming.language.primary.rank.Visual Basic": 178,
#         "programming.language.primary.rank.Scala": 179,
#         "programming.language.primary.rank.Go": 180,
#         "programming.language.primary.rank.HTML / CSS": 181,
#         "programming.language.primary.rank.Haskell": 182,
#         "programming.language.primary.rank.R": 183,
#         "programming.language.primary.rank.SQL<br />(PL/SQL, T-SQL and other<br />programming extensions over SQL)": 184,
#         "programming.language.primary.rank.TypeScript": 185,
#         "programming.language.primary.rank.Dart": 186,
#         "programming.language.primary.rank.CoffeeScript": 187,
#         "programming.language.primary.rank.Clojure / ClojureScript": 188,
#         "programming.language.primary.rank.Delphi": 189,
#         "programming.language.primary.rank.Cobol": 190,
#         "programming.language.primary.rank.Groovy": 191,
#         "programming.language.primary.rank.Rust": 192,
#         "programming.language.primary.rank.Ceylon": 193,
#         "programming.language.primary.rank.Perl": 194,
#         "programming.language.primary.rank.Assembly": 195,
#         "programming.language.primary.rank.Matlab": 196,
#         "programming.language.primary.rank.Lua": 197,
#         "programming.language.primary.rank.Shell scripting languages<br />(bash/shell/powershell)": 198,
#         "programming.language.primary.rank.Julia": 199,
#         "programming.language.primary.rank.F#": 200
#     },
#     "unit.testing": {
#         "unit.testing": 201
#     },
#     "database": {
#         "database.None": 202,
#         "database.DB2": 203,
#         "database.MS SQL Server": 204,
#         "database.MySQL": 205,
#         "database.Oracle Database": 206,
#         "database.PostgreSQL": 207,
#         "database.SQLite": 208,
#         "database.Cassandra": 209,
#         "database.Couchbase": 210,
#         "database.HBase": 211,
#         "database.MongoDB": 212,
#         "database.Neo4j": 213,
#         "database.Redis": 214,
#         "database.Amazon Redshift": 215,
#         "database.h2": 216,
#         "database.Other - Write In": 217,
#         "database.migrate.DB2": 218,
#         "database.migrate.MS SQL Server": 219,
#         "database.migrate.SQLite": 220,
#         "database.migrate.Oracle Database": 221,
#         "database.migrate.PostgreSQL": 222,
#         "database.migrate.MySQL": 223,
#         "database.migrate.MongoDB": 224,
#         "database.migrate.Redis": 225,
#         "database.migrate.Cassandra": 226,
#         "database.migrate.HBase": 227,
#         "database.migrate.Neo4j": 228,
#         "database.migrate.Couchbase": 229,
#         "database.migrate.Amazon Redshift": 230,
#         "database.migrate.h2": 231,
#         "database.migrate.Yes, planning to adopt / migrate to other database(s) - Write in": 232,
#         "database.migrate.No, not planning to adopt / migrate": 233
#     },
#     "database.migrate": {
#         "database.migrate.DB2": 218,
#         "database.migrate.MS SQL Server": 219,
#         "database.migrate.SQLite": 220,
#         "database.migrate.Oracle Database": 221,
#         "database.migrate.PostgreSQL": 222,
#         "database.migrate.MySQL": 223,
#         "database.migrate.MongoDB": 224,
#         "database.migrate.Redis": 225,
#         "database.migrate.Cassandra": 226,
#         "database.migrate.HBase": 227,
#         "database.migrate.Neo4j": 228,
#         "database.migrate.Couchbase": 229,
#         "database.migrate.Amazon Redshift": 230,
#         "database.migrate.h2": 231,
#         "database.migrate.Yes, planning to adopt / migrate to other database(s) - Write in": 232,
#         "database.migrate.No, not planning to adopt / migrate": 233
#     },
#     "db.app.host": {
#         "db.app.host.Locally (on your workstation, developer environment or device)": 234,
#         "db.app.host.Private Servers (hosted on your companys cluster or server on-premises)": 235,
#         "db.app.host.Amazon Web Services": 236,
#         "db.app.host.Microsoft Azure": 237,
#         "db.app.host.Google Cloud Platform": 238,
#         "db.app.host.Rackspace": 239,
#         "db.app.host.RedHat OpenShift": 240,
#         "db.app.host.IBM SoftLayer": 241,
#         "db.app.host.Cloud Foundry": 242,
#         "db.app.host.Heroku": 243,
#         "db.app.host.Other - Write In": 244,
#         "db.app.host.migrate.Locally (on your workstation, developer environment or device)": 245,
#         "db.app.host.migrate.Private Servers (hosted on your companys cluster or server on-premises)": 246,
#         "db.app.host.migrate.Amazon Web Services": 247,
#         "db.app.host.migrate.Microsoft Azure": 248,
#         "db.app.host.migrate.Google Cloud Platform": 249,
#         "db.app.host.migrate.Rackspace": 250,
#         "db.app.host.migrate.RedHat OpenShift": 251,
#         "db.app.host.migrate.IBM SoftLayer": 252,
#         "db.app.host.migrate.Cloud Foundry": 253,
#         "db.app.host.migrate.Heroku": 254,
#         "db.app.host.migrate.Other - Write In": 255
#     },
#     "db.app.host.migrate": {
#         "db.app.host.migrate.Locally (on your workstation, developer environment or device)": 245,
#         "db.app.host.migrate.Private Servers (hosted on your companys cluster or server on-premises)": 246,
#         "db.app.host.migrate.Amazon Web Services": 247,
#         "db.app.host.migrate.Microsoft Azure": 248,
#         "db.app.host.migrate.Google Cloud Platform": 249,
#         "db.app.host.migrate.Rackspace": 250,
#         "db.app.host.migrate.RedHat OpenShift": 251,
#         "db.app.host.migrate.IBM SoftLayer": 252,
#         "db.app.host.migrate.Cloud Foundry": 253,
#         "db.app.host.migrate.Heroku": 254,
#         "db.app.host.migrate.Other - Write In": 255
#     },
#     "tool": {
#         "tool.Source code collaboration tool (e.g. GitHub, GitLab, Bitbucket)": 256,
#         "tool.Issue tracker (e.g. Jira, YouTrack)": 257,
#         "tool.Code review tool (e.g. Crucible, Upsource)": 258,
#         "tool.Continuous Integration (CI) or Continuous Delivery (CD) tool (e.g. Jenkins, TeamCity)": 259,
#         "tool.Static analysis tool (e.g. CodeClimate)": 260,
#         "tool.IDE (e.g. Eclipse, IntelliJ IDEA)": 261,
#         "tool.Lightweight Desktop Editor (e.g. Sublime Text, Atom, VS Code, Vim)": 262,
#         "tool.In-cloud Editor or IDE": 263,
#         "tool.None": 264,
#         "tool.ide.RStudio": 265,
#         "tool.ide.IntelliJ IDEA": 266,
#         "tool.ide.Android Studio": 267,
#         "tool.ide.Visual Studio": 268,
#         "tool.ide.Xcode": 269,
#         "tool.ide.PhpStorm": 270,
#         "tool.ide.WebStorm": 271,
#         "tool.ide.RubyMine": 272,
#         "tool.ide.PyCharm": 273,
#         "tool.ide.Vi/Vim": 274,
#         "tool.ide.Sublime Text": 275,
#         "tool.ide.Atom": 276,
#         "tool.ide.VS Code (Visual Studio Code)": 277,
#         "tool.ide.Notepad++": 278,
#         "tool.ide.AppCode": 279,
#         "tool.ide.CLion": 280,
#         "tool.ide.Eclipse": 281,
#         "tool.ide.NetBeans": 282,
#         "tool.ide.QtCreator": 283,
#         "tool.ide.Emacs": 284,
#         "tool.ide.TextMate": 285,
#         "tool.ide.JetBrains Rider": 286,
#         "tool.ide.Gedit": 287,
#         "tool.ide.KDevelop": 288,
#         "tool.ide.PHPEdit": 289,
#         "tool.ide.Coda": 290,
#         "tool.ide.IPython/Jupyter Notebook": 291,
#         "tool.ide.Zend Studio": 292,
#         "tool.ide.Aptana": 293,
#         "tool.ide.BBEdit": 294,
#         "tool.ide.Other - Write In": 295,
#         "tool.team.adopted.Source code collaboration tool (e.g. GitHub, GitLab, Bitbucket)": 296,
#         "tool.team.adopted.Issue tracker (e.g. Jira, YouTrack)": 297,
#         "tool.team.adopted.Code review tool (e.g. Crucible, Upsource)": 298,
#         "tool.team.adopted.Continuous Integration (CI) or Continuous Delivery (CD) tool (e.g. Jenkins, TeamCity)": 299,
#         "tool.team.adopted.Static analysis tool (e.g. CodeClimate)": 300,
#         "tool.team.adopted.IDE (e.g. Eclipse, IntelliJ IDEA)": 301,
#         "tool.team.adopted.Lightweight Desktop Editor (e.g. Sublime Text, Atom, VS Code, Vim)": 302,
#         "tool.team.adopted.In-cloud Editor or IDE": 303,
#         "tool.team.adopted.None": 304,
#         "tool.type.source.code.collaboration.Paid": 305,
#         "tool.type.source.code.collaboration.Free": 306,
#         "tool.type.source.code.collaboration.Not sure": 307,
#         "tool.type.issue.tracker.Paid": 308,
#         "tool.type.issue.tracker.Free": 309,
#         "tool.type.issue.tracker.Not sure": 310,
#         "tool.type.code.review.Paid": 311,
#         "tool.type.code.review.Free": 312,
#         "tool.type.code.review.Not sure": 313,
#         "tool.type.ci.Paid": 314,
#         "tool.type.ci.Free": 315,
#         "tool.type.ci.Not sure": 316,
#         "tool.type.static.analysis.Paid": 317,
#         "tool.type.static.analysis.Free": 318,
#         "tool.type.static.analysis.Not sure": 319,
#         "tool.type.ide.Paid": 320,
#         "tool.type.ide.Free": 321,
#         "tool.type.ide.Not sure": 322,
#         "tool.type.text.editor.Paid": 323,
#         "tool.type.text.editor.Free": 324,
#         "tool.type.text.editor.Not sure": 325,
#         "tool.type.cloud.ide.editor.Paid": 326,
#         "tool.type.cloud.ide.editor.Free": 327,
#         "tool.type.cloud.ide.editor.Not sure": 328,
#         "tool.ci.Jenkins / Hudson": 329,
#         "tool.ci.TeamCity": 330,
#         "tool.ci.Bamboo": 331,
#         "tool.ci.Microsoft Team Foundation Build": 332,
#         "tool.ci.Travis CI": 333,
#         "tool.ci.CodeShip": 334,
#         "tool.ci.Codeship": 335,
#         "tool.ci.CircleCI": 336,
#         "tool.ci.CruiseControl": 337,
#         "tool.ci.GoCD": 338,
#         "tool.ci.Gitlab CI": 339,
#         "tool.ci.Microsoft TFS / Visual Studio Team Services": 340,
#         "tool.ci.AppVeyor": 341,
#         "tool.ci.Drone": 342,
#         "tool.ci.Semaphore CI": 343,
#         "tool.ci.Other - Write In": 344,
#         "tool.issue.tracker.Jira": 345,
#         "tool.issue.tracker.YouTrack": 346,
#         "tool.issue.tracker.Redmine": 347,
#         "tool.issue.tracker.GitLab Issue Board": 348,
#         "tool.issue.tracker.Asana": 349,
#         "tool.issue.tracker.Wrike": 350,
#         "tool.issue.tracker.Microsoft TFS / Visual Studio Team Services": 351,
#         "tool.issue.tracker.Trello": 352,
#         "tool.issue.tracker.GitHub Issues": 353,
#         "tool.issue.tracker.Other - Write In": 354,
#         "tool.use.in.cloud.None": 355,
#         "tool.use.in.cloud.Continuous Integration tool": 356,
#         "tool.use.in.cloud.Continuous Delivery tool": 357,
#         "tool.use.in.cloud.Code Review tool": 358,
#         "tool.use.in.cloud.Issue Tracker": 359,
#         "tool.version.control.system.None": 360,
#         "tool.version.control.system.Concurrent Versions System (CVS)": 361,
#         "tool.version.control.system.Apache Subversion (SVN)": 362,
#         "tool.version.control.system.Git": 363,
#         "tool.version.control.system.Mercurial": 364,
#         "tool.version.control.system.Bazaar": 365,
#         "tool.version.control.system.Perforce": 366,
#         "tool.version.control.system.Other - Write In": 367,
#         "tool.where.keep.code.Version control as a service (e.g. GitHub, Bitbucket)": 368,
#         "tool.where.keep.code.Manually deployed version control (e.g. GitHub Enterprise, GitLab)": 369,
#         "tool.where.keep.code.Other - Write In": 370,
#         "tool.version.control.service.None": 371,
#         "tool.version.control.service.GitHub": 372,
#         "tool.version.control.service.GitLab": 373,
#         "tool.version.control.service.Bitbucket": 374,
#         "tool.version.control.service.Perforce": 375,
#         "tool.version.control.service.Amazon CodeCommit": 376,
#         "tool.version.control.service.RhodeCode": 377,
#         "tool.version.control.service.SourceForge": 378,
#         "tool.version.control.service.Custom tool": 379,
#         "tool.version.control.service.Microsoft TFS / Visual Studio Team Services": 380,
#         "tool.version.control.service.other": 381
#     },
#     "tool.ide": {
#         "tool.ide.RStudio": 265,
#         "tool.ide.IntelliJ IDEA": 266,
#         "tool.ide.Android Studio": 267,
#         "tool.ide.Visual Studio": 268,
#         "tool.ide.Xcode": 269,
#         "tool.ide.PhpStorm": 270,
#         "tool.ide.WebStorm": 271,
#         "tool.ide.RubyMine": 272,
#         "tool.ide.PyCharm": 273,
#         "tool.ide.Vi/Vim": 274,
#         "tool.ide.Sublime Text": 275,
#         "tool.ide.Atom": 276,
#         "tool.ide.VS Code (Visual Studio Code)": 277,
#         "tool.ide.Notepad++": 278,
#         "tool.ide.AppCode": 279,
#         "tool.ide.CLion": 280,
#         "tool.ide.Eclipse": 281,
#         "tool.ide.NetBeans": 282,
#         "tool.ide.QtCreator": 283,
#         "tool.ide.Emacs": 284,
#         "tool.ide.TextMate": 285,
#         "tool.ide.JetBrains Rider": 286,
#         "tool.ide.Gedit": 287,
#         "tool.ide.KDevelop": 288,
#         "tool.ide.PHPEdit": 289,
#         "tool.ide.Coda": 290,
#         "tool.ide.IPython/Jupyter Notebook": 291,
#         "tool.ide.Zend Studio": 292,
#         "tool.ide.Aptana": 293,
#         "tool.ide.BBEdit": 294,
#         "tool.ide.Other - Write In": 295
#     },
#     "tool.team.adopted": {
#         "tool.team.adopted.Source code collaboration tool (e.g. GitHub, GitLab, Bitbucket)": 296,
#         "tool.team.adopted.Issue tracker (e.g. Jira, YouTrack)": 297,
#         "tool.team.adopted.Code review tool (e.g. Crucible, Upsource)": 298,
#         "tool.team.adopted.Continuous Integration (CI) or Continuous Delivery (CD) tool (e.g. Jenkins, TeamCity)": 299,
#         "tool.team.adopted.Static analysis tool (e.g. CodeClimate)": 300,
#         "tool.team.adopted.IDE (e.g. Eclipse, IntelliJ IDEA)": 301,
#         "tool.team.adopted.Lightweight Desktop Editor (e.g. Sublime Text, Atom, VS Code, Vim)": 302,
#         "tool.team.adopted.In-cloud Editor or IDE": 303,
#         "tool.team.adopted.None": 304
#     },
#     "tool.type.source.code.collaboration": {
#         "tool.type.source.code.collaboration.Paid": 305,
#         "tool.type.source.code.collaboration.Free": 306,
#         "tool.type.source.code.collaboration.Not sure": 307
#     },
#     "tool.type.issue.tracker": {
#         "tool.type.issue.tracker.Paid": 308,
#         "tool.type.issue.tracker.Free": 309,
#         "tool.type.issue.tracker.Not sure": 310
#     },
#     "tool.type.code.review": {
#         "tool.type.code.review.Paid": 311,
#         "tool.type.code.review.Free": 312,
#         "tool.type.code.review.Not sure": 313
#     },
#     "tool.type.ci": {
#         "tool.type.ci.Paid": 314,
#         "tool.type.ci.Free": 315,
#         "tool.type.ci.Not sure": 316
#     },
#     "tool.type.static.analysis": {
#         "tool.type.static.analysis.Paid": 317,
#         "tool.type.static.analysis.Free": 318,
#         "tool.type.static.analysis.Not sure": 319
#     },
#     "tool.type.ide": {
#         "tool.type.ide.Paid": 320,
#         "tool.type.ide.Free": 321,
#         "tool.type.ide.Not sure": 322
#     },
#     "tool.type.text.editor": {
#         "tool.type.text.editor.Paid": 323,
#         "tool.type.text.editor.Free": 324,
#         "tool.type.text.editor.Not sure": 325
#     },
#     "tool.type.cloud.ide.editor": {
#         "tool.type.cloud.ide.editor.Paid": 326,
#         "tool.type.cloud.ide.editor.Free": 327,
#         "tool.type.cloud.ide.editor.Not sure": 328
#     },
#     "tool.ci": {
#         "tool.ci.Jenkins / Hudson": 329,
#         "tool.ci.TeamCity": 330,
#         "tool.ci.Bamboo": 331,
#         "tool.ci.Microsoft Team Foundation Build": 332,
#         "tool.ci.Travis CI": 333,
#         "tool.ci.CodeShip": 334,
#         "tool.ci.Codeship": 335,
#         "tool.ci.CircleCI": 336,
#         "tool.ci.CruiseControl": 337,
#         "tool.ci.GoCD": 338,
#         "tool.ci.Gitlab CI": 339,
#         "tool.ci.Microsoft TFS / Visual Studio Team Services": 340,
#         "tool.ci.AppVeyor": 341,
#         "tool.ci.Drone": 342,
#         "tool.ci.Semaphore CI": 343,
#         "tool.ci.Other - Write In": 344
#     },
#     "tool.issue.tracker": {
#         "tool.issue.tracker.Jira": 345,
#         "tool.issue.tracker.YouTrack": 346,
#         "tool.issue.tracker.Redmine": 347,
#         "tool.issue.tracker.GitLab Issue Board": 348,
#         "tool.issue.tracker.Asana": 349,
#         "tool.issue.tracker.Wrike": 350,
#         "tool.issue.tracker.Microsoft TFS / Visual Studio Team Services": 351,
#         "tool.issue.tracker.Trello": 352,
#         "tool.issue.tracker.GitHub Issues": 353,
#         "tool.issue.tracker.Other - Write In": 354
#     },
#     "tool.use.in.cloud": {
#         "tool.use.in.cloud.None": 355,
#         "tool.use.in.cloud.Continuous Integration tool": 356,
#         "tool.use.in.cloud.Continuous Delivery tool": 357,
#         "tool.use.in.cloud.Code Review tool": 358,
#         "tool.use.in.cloud.Issue Tracker": 359
#     },
#     "tool.version.control.system": {
#         "tool.version.control.system.None": 360,
#         "tool.version.control.system.Concurrent Versions System (CVS)": 361,
#         "tool.version.control.system.Apache Subversion (SVN)": 362,
#         "tool.version.control.system.Git": 363,
#         "tool.version.control.system.Mercurial": 364,
#         "tool.version.control.system.Bazaar": 365,
#         "tool.version.control.system.Perforce": 366,
#         "tool.version.control.system.Other - Write In": 367
#     },
#     "tool.where.keep.code": {
#         "tool.where.keep.code.Version control as a service (e.g. GitHub, Bitbucket)": 368,
#         "tool.where.keep.code.Manually deployed version control (e.g. GitHub Enterprise, GitLab)": 369,
#         "tool.where.keep.code.Other - Write In": 370
#     },
#     "tool.version.control.service": {
#         "tool.version.control.service.None": 371,
#         "tool.version.control.service.GitHub": 372,
#         "tool.version.control.service.GitLab": 373,
#         "tool.version.control.service.Bitbucket": 374,
#         "tool.version.control.service.Perforce": 375,
#         "tool.version.control.service.Amazon CodeCommit": 376,
#         "tool.version.control.service.RhodeCode": 377,
#         "tool.version.control.service.SourceForge": 378,
#         "tool.version.control.service.Custom tool": 379,
#         "tool.version.control.service.Microsoft TFS / Visual Studio Team Services": 380,
#         "tool.version.control.service.other": 381
#     },
#     "customise.ide": {
#         "customise.ide.No": 382,
#         "customise.ide.Yes, I use custom color schemes": 383,
#         "customise.ide.Yes, I use custom keymaps": 384,
#         "customise.ide.Yes, I use plugins": 385,
#         "customise.ide.Other - Write In": 386
#     },
#     "listen.music": {
#         "listen.music": 387
#     },
#     "music.genre": {
#         "music.genre.Heavy metal": 388,
#         "music.genre.Rock n' Roll": 389,
#         "music.genre.Rock": 390,
#         "music.genre.Alternative": 391,
#         "music.genre.Classical": 392,
#         "music.genre.Punk Rock": 393,
#         "music.genre.Blues": 394,
#         "music.genre.Rap": 395,
#         "music.genre.Jazz": 396,
#         "music.genre.Pop": 397,
#         "music.genre.Electronic": 398,
#         "music.genre.R&B": 399,
#         "music.genre.Indie": 400,
#         "music.genre.Hip Hop": 401,
#         "music.genre.Other - Write In": 402
#     },
#     "java.version": {
#         "java.version.Java 9": 403,
#         "java.version.Java 8": 404,
#         "java.version.Java 7": 405,
#         "java.version.Java 6": 406,
#         "java.version.Other - Write In": 407
#     },
#     "java.app.server": {
#         "java.app.server.None": 408,
#         "java.app.server.Apache Tomcat": 409,
#         "java.app.server.Jetty": 410,
#         "java.app.server.Wildfly": 411,
#         "java.app.server.JBoss EAP": 412,
#         "java.app.server.Weblogic": 413,
#         "java.app.server.WebSphere": 414,
#         "java.app.server.Liberty": 415,
#         "java.app.server.Glassfish": 416,
#         "java.app.server.Payara": 417,
#         "java.app.server.Other - Write In": 418
#     },
#     "java.framework.app.server": {
#         "java.framework.app.server.None": 419,
#         "java.framework.app.server.Netty": 420,
#         "java.framework.app.server.Undertow": 421,
#         "java.framework.app.server.Vert.x": 422,
#         "java.framework.app.server.Spark Java": 423,
#         "java.framework.app.server.Spring Boot": 424,
#         "java.framework.app.server.Other - Write In": 425
#     },
#     "java.package": {
#         "java.package.As artifacts (e.g. WAR)": 426,
#         "java.package.I use an embedded server (e.g. JAR)": 427,
#         "java.package.I'm not sure": 428,
#         "java.package.JUnit": 429,
#         "java.package.TestNG": 430,
#         "java.package.Mockito": 431,
#         "java.package.PowerMock": 432,
#         "java.package.Spock": 433,
#         "java.package.EasyMock": 434,
#         "java.package.JMockit": 435,
#         "java.package.Other - Write In": 436
#     },
#     "java.web.framework": {
#         "java.web.framework.None": 437,
#         "java.web.framework.Spring MVC": 438,
#         "java.web.framework.GWT": 439,
#         "java.web.framework.Vaadin": 440,
#         "java.web.framework.Play Framework": 441,
#         "java.web.framework.Grails 2": 442,
#         "java.web.framework.Grails 3": 443,
#         "java.web.framework.Spring Boot": 444,
#         "java.web.framework.JSF": 445,
#         "java.web.framework.Struts 1": 446,
#         "java.web.framework.Struts 2": 447,
#         "java.web.framework.Wicket": 448,
#         "java.web.framework.Dropwizard": 449,
#         "java.web.framework.Other - Write In": 450
#     },
#     "java.build.system": {
#         "java.build.system.None": 451,
#         "java.build.system.Maven": 452,
#         "java.build.system.sbt": 453,
#         "java.build.system.Gradle": 454,
#         "java.build.system.Ant": 455,
#         "java.build.system.Other - Write In": 456
#     },
#     "java.ee.version": {
#         "java.ee.version.None": 457,
#         "java.ee.version.Java EE 8": 458,
#         "java.ee.version.Java EE 7": 459,
#         "java.ee.version.Java EE 6": 460,
#         "java.ee.version.Java EE 5": 461,
#         "java.ee.version.J2SE": 462,
#         "java.ee.version.Other - Write In": 463
#     },
#     "java.jvm.profiler": {
#         "java.jvm.profiler.None": 464,
#         "java.jvm.profiler.VisualVM": 465,
#         "java.jvm.profiler.JProfiler": 466,
#         "java.jvm.profiler.Java Mission Control": 467,
#         "java.jvm.profiler.YourKit": 468,
#         "java.jvm.profiler.NetBeans profiler": 469,
#         "java.jvm.profiler.Honest profiler": 470,
#         "java.jvm.profiler.async-profiler": 471,
#         "java.jvm.profiler.Own custom tools": 472,
#         "java.jvm.profiler.Other - Write In": 473
#     },
#     "java.ide": {
#         "java.ide": 474
#     },
#     "java.multiple.projects": {
#         "java.multiple.projects": 475
#     },
#     "c.standard": {
#         "c.standard.C99": 476,
#         "c.standard.C11": 477,
#         "c.standard.Embedded C": 478,
#         "c.standard.Other - Write In": 479
#     },
#     "c.ide": {
#         "c.ide": 480
#     },
#     "c.unit.testing.framework": {
#         "c.unit.testing.framework.None": 481,
#         "c.unit.testing.framework.Catch": 482,
#         "c.unit.testing.framework.Boost.Test": 483,
#         "c.unit.testing.framework.Google Test": 484,
#         "c.unit.testing.framework.CppUnit": 485,
#         "c.unit.testing.framework.CppUTest": 486
#     },
#     "c.unit.testing": {
#         "c.unit.testing.framework.None": 481,
#         "c.unit.testing.framework.Catch": 482,
#         "c.unit.testing.framework.Boost.Test": 483,
#         "c.unit.testing.framework.Google Test": 484,
#         "c.unit.testing.framework.CppUnit": 485,
#         "c.unit.testing.framework.CppUTest": 486,
#         "c.unit.testing.CUnit": 487,
#         "c.unit.testing.Unity": 488,
#         "c.unit.testing.Other - Write In": 489
#     },
#     "c.project.model": {
#         "c.project.model.None": 490,
#         "c.project.model.Visual Studio project": 491,
#         "c.project.model.Xcode project": 492,
#         "c.project.model.Autotools": 493,
#         "c.project.model.Makefiles": 494,
#         "c.project.model.CMake": 495,
#         "c.project.model.Qmake": 496,
#         "c.project.model.SCons": 497,
#         "c.project.model.Boost.Build": 498,
#         "c.project.model.Basel": 499,
#         "c.project.model.Custom": 500,
#         "c.project.model.Other - Write In": 501
#     },
#     "c.compiler": {
#         "c.compiler.GCC": 502,
#         "c.compiler.Clang": 503,
#         "c.compiler.MSVC": 504,
#         "c.compiler.Intel": 505,
#         "c.compiler.Compiler for microcontrollers (like Keil, C51 C Compiler, IAR, etc.)": 506,
#         "c.compiler.Custom": 507,
#         "c.compiler.Other - Write In": 508
#     },
#     "cpp.standard": {
#         "cpp.standard.C++98": 509,
#         "cpp.standard.C++03": 510,
#         "cpp.standard.C++11": 511,
#         "cpp.standard.C++14": 512,
#         "cpp.standard.C++17": 513,
#         "cpp.standard.migrate": 514
#     },
#     "cpp.standard.migrate": {
#         "cpp.standard.migrate": 514
#     },
#     "cpp.ide": {
#         "cpp.ide": 515
#     },
#     "cpp.unit.testing": {
#         "cpp.unit.testing.None": 516,
#         "cpp.unit.testing.Boost.Test": 517,
#         "cpp.unit.testing.Google Test": 518,
#         "cpp.unit.testing.CppUnit": 519,
#         "cpp.unit.testing.CppUTest": 520,
#         "cpp.unit.testing.Catch": 521,
#         "cpp.unit.testing.Other - Write In": 522
#     },
#     "cpp.project.model": {
#         "cpp.project.model.None": 523,
#         "cpp.project.model.Visual Studio project": 524,
#         "cpp.project.model.Xcode project": 525,
#         "cpp.project.model.Autotools": 526,
#         "cpp.project.model.Makefiles": 527,
#         "cpp.project.model.CMake": 528,
#         "cpp.project.model.Qmake": 529,
#         "cpp.project.model.SCons": 530,
#         "cpp.project.model.Boost.Build": 531,
#         "cpp.project.model.Basel": 532,
#         "cpp.project.model.Custom": 533,
#         "cpp.project.model.Other - Write In": 534
#     },
#     "cpp.compiler": {
#         "cpp.compiler.GCC": 535,
#         "cpp.compiler.Clang": 536,
#         "cpp.compiler.MSVC": 537,
#         "cpp.compiler.Intel": 538,
#         "cpp.compiler.Custom": 539,
#         "cpp.compiler.Other - Write In": 540
#     },
#     "cpp.project.size": {
#         "cpp.project.size": 541
#     },
#     "python.version": {
#         "python.version": 542
#     },
#     "python.purposes": {
#         "python.purposes.Educational purposes": 543,
#         "python.purposes.Data analysis": 544,
#         "python.purposes.System administration / Writing automation scripts / Infrastructure configuration (DevOps)": 545,
#         "python.purposes.Software testing / writing automated tests": 546,
#         "python.purposes.Software prototyping": 547,
#         "python.purposes.Web development": 548,
#         "python.purposes.Programming of web parsers / scrapers / crawlers": 549,
#         "python.purposes.Machine learning": 550,
#         "python.purposes.Network programming": 551,
#         "python.purposes.Desktop development": 552,
#         "python.purposes.Computer graphics": 553,
#         "python.purposes.Game development": 554,
#         "python.purposes.Mobile development": 555,
#         "python.purposes.Embedded development": 556,
#         "python.purposes.Other - Write In": 557
#     },
#     "python.libraries": {
#         "python.libraries.NumPy / matplotlib / SciPy / Pandas and similar": 558,
#         "python.libraries.Anaconda": 559,
#         "python.libraries.Django": 560,
#         "python.libraries.Flask": 561,
#         "python.libraries.Requests": 562,
#         "python.libraries.PyQT/PyGTK/wxPython": 563,
#         "python.libraries.Keras /Theano/ TensorFlow/ scikit-learn and similar": 564,
#         "python.libraries.TkInter": 565,
#         "python.libraries.asyncio": 566,
#         "python.libraries.aiohttp": 567,
#         "python.libraries.six": 568,
#         "python.libraries.Twisted": 569,
#         "python.libraries.SQLAlchemy": 570,
#         "python.libraries.Scrapy": 571,
#         "python.libraries.Pygame": 572,
#         "python.libraries.Pillow": 573,
#         "python.libraries.Sphinx": 574,
#         "python.libraries.Web2py": 575,
#         "python.libraries.Tornado": 576,
#         "python.libraries.Bottle": 577,
#         "python.libraries.Kivy": 578,
#         "python.libraries.CherryPy": 579,
#         "python.libraries.Pyramid": 580,
#         "python.libraries.Other - Write In": 581
#     },
#     "python.techs": {
#         "python.techs.None": 582,
#         "python.techs.Sphinx": 583,
#         "python.techs.Buildout": 584,
#         "python.techs.ORM": 585,
#         "python.techs.Other - Write In": 586
#     },
#     "python.ide": {
#         "python.ide": 587
#     },
#     "python.how.often": {
#         "python.how.often.Use autocompletion in your editor": 588,
#         "python.how.often.Use the debugger": 589,
#         "python.how.often.Refactor your code": 590,
#         "python.how.often.Use code linting (programs that analyze code for potential errors)": 591,
#         "python.how.often.Use Python virtual environments for your projects": 592,
#         "python.how.often.Run / debug or edit code on remote machines (remote hosts, VMs, etc.)": 593,
#         "python.how.often.Use a Python profiler": 594,
#         "python.how.often.Use code coverage": 595,
#         "python.how.often.Use optional type hinting": 596,
#         "python.how.often.Use Issue Trackers": 597
#     },
#     "csharp.version": {
#         "csharp.version.C# 5 (async / await, caller info attributes)": 598,
#         "csharp.version.C# 6 (? and nameof operators, static imports, exception filters, Roslyn)": 599,
#         "csharp.version.C# 7 (pattern matching, local functions, ref locals and returns, out variables)": 600,
#         "csharp.version.Earlier version": 601,
#         "csharp.version.I'm not sure": 602
#     },
#     "csharp.runtime": {
#         "csharp.runtime.NET Framework": 603,
#         "csharp.runtime.Mono": 604,
#         "csharp.runtime.NET Core": 605
#     },
#     "csharp.framework": {
#         "csharp.framework.None": 606,
#         "csharp.framework.Sharepoint": 607,
#         "csharp.framework.ASP.NET MVC": 608,
#         "csharp.framework.ASP.NET Web Forms": 609,
#         "csharp.framework.ASP.NET Core": 610,
#         "csharp.framework.Windows Presentation Foundation (WPF)": 611,
#         "csharp.framework.Windows Forms": 612,
#         "csharp.framework.Windows Communication Foundation (WCF)": 613,
#         "csharp.framework.Entity Framework": 614,
#         "csharp.framework.Unity3d": 615,
#         "csharp.framework.Xamarin": 616,
#         "csharp.framework.UWP": 617,
#         "csharp.framework.Azure": 618,
#         "csharp.framework.Other - Write In": 619
#     },
#     "csharp.ide": {
#         "csharp.ide": 620
#     },
#     "csharp.dev.environment": {
#         "csharp.dev.environment.Windows": 621,
#         "csharp.dev.environment.Unix / Linux": 622,
#         "csharp.dev.environment.macOS": 623
#     },
#     "csharp.visual.studio.version": {
#         "csharp.visual.studio.version": 624
#     },
#     "csharp.unit.testing": {
#         "csharp.unit.testing.None": 625,
#         "csharp.unit.testing.MSTest/Visual Studio Unit Testing Framework": 626,
#         "csharp.unit.testing.MSTest V2": 627,
#         "csharp.unit.testing.NUnit": 628,
#         "csharp.unit.testing.xUnit": 629,
#         "csharp.unit.testing.other": 630
#     },
#     "csharp.tools": {
#         "csharp.tools.None": 631,
#         "csharp.tools.YourKit Profiler": 632,
#         "csharp.tools.PerfView": 633,
#         "csharp.tools.Intel VTune Amplifier": 634,
#         "csharp.tools.SciTech .NET memory profiler": 635,
#         "csharp.tools.Windows Performance Toolkit": 636,
#         "csharp.tools.Visual Studio's built-in performance and diagnostic tools": 637,
#         "csharp.tools.dotTrace": 638,
#         "csharp.tools.dotMemory": 639,
#         "csharp.tools.ANTS Profiler": 640,
#         "csharp.tools.Other - Write In": 641
#     },
#     "csharp.msdn.subscription": {
#         "csharp.msdn.subscription": 642
#     },
#     "csharp.tfs.vsts": {
#         "csharp.tfs.vsts": 643
#     },
#     "php.version": {
#         "php.version": 644
#     },
#     "php.environment": {
#         "php.environment.Local environment": 645,
#         "php.environment.Remote environment (SFTP, SSH, Remote desktop, etc.)": 646,
#         "php.environment.Virtualized environment (Vagrant, Otto, etc.)": 647,
#         "php.environment.Containerized environment (Docker, Rocket)": 648,
#         "php.environment.Other - Write In": 649
#     },
#     "php.debugger": {
#         "php.debugger": 650
#     },
#     "php.frameworks": {
#         "php.frameworks.None": 651,
#         "php.frameworks.Symfony": 652,
#         "php.frameworks.Drupal": 653,
#         "php.frameworks.WordPress": 654,
#         "php.frameworks.Zend": 655,
#         "php.frameworks.Magento": 656,
#         "php.frameworks.Laravel": 657,
#         "php.frameworks.Joomla!": 658,
#         "php.frameworks.Yii": 659,
#         "php.frameworks.CakePHP": 660,
#         "php.frameworks.codeigniter": 661,
#         "php.frameworks.slim": 662,
#         "php.frameworks.Other - Write In": 663
#     },
#     "php.ide": {
#         "php.ide": 664
#     },
#     "php.unit.testing": {
#         "php.unit.testing.None": 665,
#         "php.unit.testing.PHPUnit": 666,
#         "php.unit.testing.Behat": 667,
#         "php.unit.testing.PHPSpec": 668,
#         "php.unit.testing.Codeception": 669,
#         "php.unit.testing.SimpleTest": 670,
#         "php.unit.testing.Other - Write In": 671
#     },
#     "kotlin.jdk.version": {
#         "kotlin.jdk.version.JDK 6": 672,
#         "kotlin.jdk.version.JDK 7": 673,
#         "kotlin.jdk.version.JDK 8": 674,
#         "kotlin.jdk.version.JDK 9 (Legacy mode)": 675,
#         "kotlin.jdk.version.JDK 9 (Jigsaw module system)": 676
#     },
#     "kotlin.android.version": {
#         "kotlin.android.version.Jelly Bean": 677,
#         "kotlin.android.version.KitKat": 678,
#         "kotlin.android.version.Lollypop": 679,
#         "kotlin.android.version.Marshmallow": 680,
#         "kotlin.android.version.Nougat": 681,
#         "kotlin.android.version.Oreo": 682
#     },
#     "kotlin.js.version": {
#         "kotlin.js.version.Browser": 683,
#         "kotlin.js.version.Node.JS": 684
#     },
#     "kotlin.version": {
#         "kotlin.version.I dont know": 685
#     },
#     "kotlin.experience": {
#         "kotlin.experience": 686
#     },
#     "kotlin.background": {
#         "kotlin.background": 687
#     },
#     "kotlin.previous.language": {
#         "kotlin.previous.language.Java": 688,
#         "kotlin.previous.language.JavaScript/TypeScript": 689,
#         "kotlin.previous.language.C/C++": 690,
#         "kotlin.previous.language.C#": 691,
#         "kotlin.previous.language.PHP": 692,
#         "kotlin.previous.language.Ruby": 693,
#         "kotlin.previous.language.Scala": 694,
#         "kotlin.previous.language.Go": 695,
#         "kotlin.previous.language.Groovy": 696,
#         "kotlin.previous.language.Python": 697,
#         "kotlin.previous.language.Swift": 698,
#         "kotlin.previous.language.Other - Write In": 699
#     },
#     "ruby.version": {
#         "ruby.version": 700,
#         "ruby.version.migrate": 701,
#         "ruby.version.manager.None": 702,
#         "ruby.version.manager.RVM": 703,
#         "ruby.version.manager.Rbenv": 704,
#         "ruby.version.manager.Ruby-build": 705,
#         "ruby.version.manager.Chruby": 706,
#         "ruby.version.manager.Other - Write In": 707
#     },
#     "ruby.version.migrate": {
#         "ruby.version.migrate": 701
#     },
#     "ruby.version.manager": {
#         "ruby.version.manager.None": 702,
#         "ruby.version.manager.RVM": 703,
#         "ruby.version.manager.Rbenv": 704,
#         "ruby.version.manager.Ruby-build": 705,
#         "ruby.version.manager.Chruby": 706,
#         "ruby.version.manager.Other - Write In": 707
#     },
#     "ruby.gem.management": {
#         "ruby.gem.management.None": 708,
#         "ruby.gem.management.Bundler": 709,
#         "ruby.gem.management.RVM gemsets": 710,
#         "ruby.gem.management.other": 711
#     },
#     "ruby.gems.count": {
#         "ruby.gems.count": 712
#     },
#     "ruby.framework": {
#         "ruby.framework.None": 713,
#         "ruby.framework.Ruby on Rails": 714,
#         "ruby.framework.Rack": 715,
#         "ruby.framework.Sinatra": 716,
#         "ruby.framework.Hanami": 717,
#         "ruby.framework.other": 718
#     },
#     "ruby.rails.version": {
#         "ruby.rails.version": 719,
#         "ruby.rails.version.migrate": 720
#     },
#     "ruby.rails.version.migrate": {
#         "ruby.rails.version.migrate": 720
#     },
#     "ruby.server": {
#         "ruby.server.None": 721,
#         "ruby.server.Unicorn": 722,
#         "ruby.server.Puma": 723,
#         "ruby.server.Passenger (mod_rails)": 724,
#         "ruby.server.Thin": 725,
#         "ruby.server.FastCGI": 726,
#         "ruby.server.Other - Write In": 727
#     },
#     "ruby.ide": {
#         "ruby.ide": 728
#     },
#     "ruby.unit.testing": {
#         "ruby.unit.testing.None": 729,
#         "ruby.unit.testing.Shoulda": 730,
#         "ruby.unit.testing.Rspec": 731,
#         "ruby.unit.testing.Cucumber": 732,
#         "ruby.unit.testing.Test": 733,
#         "ruby.unit.testing.Other - Write In": 734
#     },
#     "swift.platform": {
#         "swift.platform.iOS": 735,
#         "swift.platform.watchOS": 736,
#         "swift.platform.other": 737
#     },
#     "swift.objectivec": {
#         "swift.objectivec": 738
#     },
#     "swift.cpp": {
#         "swift.cpp": 739
#     },
#     "swift.version": {
#         "swift.version": 740,
#         "swift.version.migrate": 741
#     },
#     "swift.version.migrate": {
#         "swift.version.migrate": 741
#     },
#     "swift.unit.testing": {
#         "swift.unit.testing.None": 742,
#         "swift.unit.testing.XCTest": 743,
#         "swift.unit.testing.Quick + Nimble": 744,
#         "swift.unit.testing.other": 745
#     },
#     "swift.ui.tests": {
#         "swift.ui.tests": 746,
#         "swift.ui.tests.framework": 747
#     },
#     "swift.ui.tests.framework": {
#         "swift.ui.tests.framework": 747
#     },
#     "swift.dependency.manager": {
#         "swift.dependency.manager": 748
#     },
#     "swift.database": {
#         "swift.database": 749,
#         "swift.database.viewer.use": 750,
#         "swift.database.viewer": 751
#     },
#     "swift.database.viewer.use": {
#         "swift.database.viewer.use": 750
#     },
#     "swift.database.viewer": {
#         "swift.database.viewer.use": 750,
#         "swift.database.viewer": 751
#     },
#     "swift.build": {
#         "swift.build": 752
#     },
#     "swift.on.linux": {
#         "swift.on.linux": 753
#     },
#     "objectivec.platform": {
#         "objectivec.platform.iOS": 754,
#         "objectivec.platform.tvOS": 755,
#         "objectivec.platform.watchOS": 756,
#         "objectivec.platform.macOS": 757,
#         "objectivec.platform.None": 760,
#         "objectivec.platform.XCTest": 761
#     },
#     "objectivec.swift": {
#         "objectivec.swift": 758
#     },
#     "objectivec.cpp": {
#         "objectivec.cpp": 759
#     },
#     "objectivec.unit.testing": {
#         "objectivec.unit.testing.other": 762
#     },
#     "objectivec.mock": {
#         "objectivec.mock": 763
#     },
#     "objectivec.ui.tests": {
#         "objectivec.ui.tests": 764
#     },
#     "objectivec.ui.test.framework": {
#         "objectivec.ui.test.framework": 765
#     },
#     "objectivec.dependency.manager": {
#         "objectivec.dependency.manager": 766
#     },
#     "objectivec.database": {
#         "objectivec.database": 767,
#         "objectivec.database.viewer.use": 768,
#         "objectivec.database.viewer": 769
#     },
#     "objectivec.database.viewer.use": {
#         "objectivec.database.viewer.use": 768
#     },
#     "objectivec.database.viewer": {
#         "objectivec.database.viewer.use": 768,
#         "objectivec.database.viewer": 769
#     },
#     "objectivec.build": {
#         "objectivec.build": 770
#     },
#     "scala.version": {
#         "scala.version.2.13": 771,
#         "scala.version.2.12": 772,
#         "scala.version.2.11": 773,
#         "scala.version.2.10 or older": 774,
#         "scala.version.other": 775
#     },
#     "scala.target": {
#         "scala.target.JVM": 776,
#         "scala.target.scala.js": 777,
#         "scala.target.Android": 778,
#         "scala.target.scala-native": 779
#     },
#     "scala.java.version": {
#         "scala.java.version.Java 9": 780,
#         "scala.java.version.Java 8": 781,
#         "scala.java.version.other": 782
#     },
#     "scala.unit.testing": {
#         "scala.unit.testing.None": 783,
#         "scala.unit.testing.ScalaTest": 784,
#         "scala.unit.testing.ScalaMock": 785,
#         "scala.unit.testing.TestNG": 786,
#         "scala.unit.testing.JUnit": 787,
#         "scala.unit.testing.ScalaCheck": 788,
#         "scala.unit.testing.specs2": 789,
#         "scala.unit.testing.other": 790
#     },
#     "scala.web.frameworks": {
#         "scala.web.frameworks.None": 791,
#         "scala.web.frameworks.Akka": 792,
#         "scala.web.frameworks.Netty": 793,
#         "scala.web.frameworks.Spark Java": 794,
#         "scala.web.frameworks.Play": 795,
#         "scala.web.frameworks.Spray": 796,
#         "scala.web.frameworks.Lift": 797,
#         "scala.web.frameworks.Scalatra": 798,
#         "scala.web.frameworks.Finatra": 799,
#         "scala.web.frameworks.Spring": 800,
#         "scala.web.frameworks.other": 801
#     },
#     "scala.frameworks": {
#         "scala.frameworks.None": 802,
#         "scala.frameworks.Scala.js": 803,
#         "scala.frameworks.Twitter Util": 804,
#         "scala.frameworks.Akka": 805,
#         "scala.frameworks.Spark": 806,
#         "scala.frameworks.Scalaz": 807,
#         "scala.frameworks.Scalacheck": 808,
#         "scala.frameworks.Specs2": 809,
#         "scala.frameworks.Shapeless": 810,
#         "scala.frameworks.Finagle": 811,
#         "scala.frameworks.Cats": 812,
#         "scala.frameworks.Breeze": 813,
#         "scala.frameworks.Slick": 814,
#         "scala.frameworks.Other - Write In": 815
#     },
#     "scala.ide": {
#         "scala.ide": 816
#     },
#     "scala.additional.ide": {
#         "scala.additional.ide": 817
#     },
#     "scala.build.system": {
#         "scala.build.system.Maven": 818,
#         "scala.build.system.Gradle": 819,
#         "scala.build.system.Ant": 820,
#         "scala.build.system.sbt": 821,
#         "scala.build.system.other": 822
#     },
#     "scala.sbt.version": {
#         "scala.sbt.version.1": 823,
#         "scala.sbt.version.0.13": 824,
#         "scala.sbt.version.0.12 or older": 825
#     },
#     "scala.interactive.env": {
#         "scala.interactive.env.None": 826,
#         "scala.interactive.env.Scala REPL": 827,
#         "scala.interactive.env.sbt console": 828,
#         "scala.interactive.env.Ammonite REPL": 829,
#         "scala.interactive.env.other": 830,
#         "scala.interactive.env.IntelliJ IDEA Worksheet": 831,
#         "scala.interactive.env.Scala IDE Worksheet": 832,
#         "scala.interactive.env.Apache Zeppelin Notebook": 833,
#         "scala.interactive.env.Jupyter Notebook": 834
#     },
#     "scala.compiler.plugins": {
#         "scala.compiler.plugins.None": 835,
#         "scala.compiler.plugins.Scalamacros/Scalameta Paradise": 836,
#         "scala.compiler.plugins.Kind Projector": 837,
#         "scala.compiler.plugins.other": 838
#     },
#     "scala.macros": {
#         "scala.macros": 839
#     },
#     "javascript.ecma6plus": {
#         "javascript.ecma6plus": 840
#     },
#     "javascript.framework": {
#         "javascript.framework.None": 841,
#         "javascript.framework.AngularJS": 842,
#         "javascript.framework.Angular 2": 843,
#         "javascript.framework.React": 844,
#         "javascript.framework.React Native": 845,
#         "javascript.framework.Cordova / PhoneGap": 846,
#         "javascript.framework.Express": 847,
#         "javascript.framework.Vue.js": 848,
#         "javascript.framework.Meteor": 849,
#         "javascript.framework.Ember": 850,
#         "javascript.framework.Backbone": 851,
#         "javascript.framework.Aurelia": 852,
#         "javascript.framework.Polymer": 853,
#         "javascript.framework.Electron": 854,
#         "javascript.framework.Other - Write In": 855
#     },
#     "javascript.ide": {
#         "javascript.ide": 856
#     },
#     "javascript.unit.testing": {
#         "javascript.unit.testing.None": 857,
#         "javascript.unit.testing.Mocha": 858,
#         "javascript.unit.testing.Jest": 859,
#         "javascript.unit.testing.Ava": 860,
#         "javascript.unit.testing.Karma": 861,
#         "javascript.unit.testing.Jasmine": 862,
#         "javascript.unit.testing.Other - Write In": 863
#     },
#     "javascript.module.loader": {
#         "javascript.module.loader.None": 864,
#         "javascript.module.loader.Browserify": 865,
#         "javascript.module.loader.Webpack": 866,
#         "javascript.module.loader.RequireJS": 867,
#         "javascript.module.loader.SystemJS": 868,
#         "javascript.module.loader.Rollup": 869,
#         "javascript.module.loader.Other - Write In": 870
#     },
#     "db.sql.server.version": {
#         "db.sql.server.version": 871
#     },
#     "db.oracle.version": {
#         "db.oracle.version": 872
#     },
#     "db.mysql.version": {
#         "db.mysql.version": 873
#     },
#     "db.postgressql.version": {
#         "db.postgressql.version": 874
#     },
#     "db.db2.version": {
#         "db.db2.version": 875
#     },
#     "db.sqlite.version": {
#         "db.sqlite.version": 876
#     },
#     "db.managing.tool": {
#         "db.managing.tool.MySQL Workbench": 877,
#         "db.managing.tool.pgAdmin": 878,
#         "db.managing.tool.Oracle SQL Developer": 879,
#         "db.managing.tool.SQL Server Management Studio": 880,
#         "db.managing.tool.DataGrip": 881,
#         "db.managing.tool.phpMyAdmin": 882,
#         "db.managing.tool.Navicat": 883,
#         "db.managing.tool.Toad": 884,
#         "db.managing.tool.EMS SQL Manager": 885,
#         "db.managing.tool.dbForge Studio": 886,
#         "db.managing.tool.HeidiSQL": 887,
#         "db.managing.tool.DbVisualizer": 888,
#         "db.managing.tool.DBeaver": 889,
#         "db.managing.tool.Sequel Pro": 890,
#         "db.managing.tool.SQuirreL SQL": 891,
#         "db.managing.tool.Command Line": 892,
#         "db.managing.tool.JetBrains IDE(s) (IntelliJ IDEA, PhpStorm, etc.) with the DataBase plugin": 893,
#         "db.managing.tool.robomongo": 894,
#         "db.managing.tool.PL / SQL Developer": 895,
#         "db.managing.tool.Other - Write In": 896
#     },
#     "go.several.versions": {
#         "go.several.versions": 897
#     },
#     "go.single.gopath": {
#         "go.single.gopath": 898
#     },
#     "go.multiple.projects": {
#         "go.multiple.projects": 899
#     },
#     "go.templates": {
#         "go.templates": 900
#     },
#     "go.package.manager": {
#         "go.package.manager.None": 901,
#         "go.package.manager.golang/dep": 902,
#         "go.package.manager.godep": 903,
#         "go.package.manager.glide": 904,
#         "go.package.manager.govendor": 905,
#         "go.package.manager.gpm": 906,
#         "go.package.manager.other": 907,
#         "go.package.manager.migrate.golang/dep": 908,
#         "go.package.manager.migrate.godep": 909,
#         "go.package.manager.migrate.glide": 910,
#         "go.package.manager.migrate.No, I don't plan to": 911,
#         "go.package.manager.migrate.other": 912
#     },
#     "go.package.manager.migrate": {
#         "go.package.manager.migrate.golang/dep": 908,
#         "go.package.manager.migrate.godep": 909,
#         "go.package.manager.migrate.glide": 910,
#         "go.package.manager.migrate.No, I don't plan to": 911,
#         "go.package.manager.migrate.other": 912
#     },
#     "go.web.frameworks": {
#         "go.web.frameworks.None": 913,
#         "go.web.frameworks.Buffalo": 914,
#         "go.web.frameworks.Gin": 915,
#         "go.web.frameworks.Macaron": 916,
#         "go.web.frameworks.Echo": 917,
#         "go.web.frameworks.Beego": 918,
#         "go.web.frameworks.Revel": 919,
#         "go.web.frameworks.other": 920
#     },
#     "go.router": {
#         "go.router.None": 921,
#         "go.router.standard library": 922,
#         "go.router.gorilla / mux": 923,
#         "go.router.go-chi / chi": 924,
#         "go.router.julienschmidt / httproute": 925,
#         "go.router.other": 926
#     },
#     "go.testing": {
#         "go.testing.None": 927,
#         "go.testing.built-in testing": 928,
#         "go.testing.gocheck": 929,
#         "go.testing.testify": 930,
#         "go.testing.ginkgo": 931,
#         "go.testing.gomega": 932,
#         "go.testing.goconvey": 933,
#         "go.testing.gomock": 934,
#         "go.testing.go-sqlmock": 935,
#         "go.testing.other": 936
#     },
#     "go.external.deps": {
#         "go.external.deps": 937
#     },
#     "go.codebase.size": {
#         "go.codebase.size": 938
#     },
#     "sleep.hours": {
#         "sleep.hours": 939
#     },
#     "devops.iaac": {
#         "devops.iaac.None": 940,
#         "devops.iaac.I dont know": 941,
#         "devops.iaac.Ad-hoc scripts": 942,
#         "devops.iaac.Configuration management tools (Puppet, Ansible, )": 943,
#         "devops.iaac.Server templating tools (Docker, Vagrant, Packer, )": 944,
#         "devops.iaac.Infrastructure provisioning tools (Terraform, CloudFormation, ..)": 945,
#         "devops.iaac.Other - Write In": 946
#     },
#     "devops.involved": {
#         "devops.involved": 947
#     },
#     "devops.configuration.management.tool": {
#         "devops.configuration.management.tool.Puppet": 948,
#         "devops.configuration.management.tool.Chef": 949,
#         "devops.configuration.management.tool.Ansible": 950,
#         "devops.configuration.management.tool.Salt": 951,
#         "devops.configuration.management.tool.Custom solution": 952,
#         "devops.configuration.management.tool.Other - Write In": 953
#     },
#     "devops.server.templating": {
#         "devops.server.templating.Docker": 954,
#         "devops.server.templating.Vagrant": 955,
#         "devops.server.templating.Packer": 956,
#         "devops.server.templating.CoreOS rkt": 957,
#         "devops.server.templating.Other - Write In": 958
#     },
#     "devops.infrastructure.provisioning": {
#         "devops.infrastructure.provisioning.Terraform": 959,
#         "devops.infrastructure.provisioning.CloudFormation": 960,
#         "devops.infrastructure.provisioning.TOSCA/Cloudify": 961,
#         "devops.infrastructure.provisioning.OpenStack Heat": 962,
#         "devops.infrastructure.provisioning.Other - Write In": 963
#     },
#     "devops.cloud.deploy": {
#         "devops.cloud.deploy.Run scripts on your local workstation / VM": 964,
#         "devops.cloud.deploy.Use Continuous Integration / Continuous Delivery": 965,
#         "devops.cloud.deploy.Use your cloud provider's web interface": 966,
#         "devops.cloud.deploy.Other - Write In": 967
#     },
#     "devops.docker.localy": {
#         "devops.docker.localy": 968
#     },
#     "devops.docker.compose": {
#         "devops.docker.compose": 969
#     },
#     "devops.container.orchestration": {
#         "devops.container.orchestration.None": 970,
#         "devops.container.orchestration.Amazon ECS / Fargate": 971,
#         "devops.container.orchestration.Amazon EKS": 972,
#         "devops.container.orchestration.Mesos or DC / OS": 973,
#         "devops.container.orchestration.Kubernetes (self-managed or fully managed)": 974,
#         "devops.container.orchestration.Hashicorp Nomad": 975,
#         "devops.container.orchestration.Docker Swarm": 976,
#         "devops.container.orchestration.CoreOS Tectonic": 977,
#         "devops.container.orchestration.Other - Write In": 978
#     },
#     "devops.docker.repository": {
#         "devops.docker.repository.I do not deploy": 979,
#         "devops.docker.repository.I use only the command line": 980,
#         "devops.docker.repository.I use a configuration management tool (Chef, Puppet, Ansible, etc.)": 981,
#         "devops.docker.repository.I deploy from CI / CD": 982,
#         "devops.docker.repository.I deploy with custom / in-house tools": 983,
#         "devops.docker.repository.Other - Write In": 984
#     },
#     "devops.artifacts": {
#         "devops.artifacts.I don't keep artifacts": 985,
#         "devops.artifacts.Pulp": 986,
#         "devops.artifacts.Amazon S3": 987,
#         "devops.artifacts.Archiva": 988,
#         "devops.artifacts.NuGet": 989,
#         "devops.artifacts.Nexus": 990,
#         "devops.artifacts.JFrog Artifactory": 991,
#         "devops.artifacts.MyGet": 992,
#         "devops.artifacts.npm": 993,
#         "devops.artifacts.Docker Hub (private or public)": 994,
#         "devops.artifacts.Custom tool": 995,
#         "devops.artifacts.Other - Write In": 996
#     },
#     "do.static.analysis": {
#         "do.static.analysis": 997
#     },
#     "do.open.source": {
#         "do.open.source": 998
#     },
#     "coding.hours.job": {
#         "coding.hours.job": 999
#     },
#     "coding.hours.personal": {
#         "coding.hours.personal": 1000
#     },
#     "coding.place": {
#         "coding.place": 1001
#     },
#     "coding.weekends": {
#         "coding.weekends": 1002
#     },
#     "have.phone": {
#         "have.phone.No": 1003,
#         "have.phone.Yes, Apple iOS": 1004,
#         "have.phone.Yes, Android": 1005,
#         "have.phone.Yes, Blackberry": 1006,
#         "have.phone.Yes, a cell phone": 1007,
#         "have.phone.Yes, Other - Write In": 1008
#     },
#     "visit.meetups": {
#         "visit.meetups": 1009
#     },
#     "programming.languages.learning": {
#         "programming.languages.learning.I am not learning any programming languages": 1010,
#         "programming.languages.learning.Java": 1011,
#         "programming.languages.learning.C": 1012,
#         "programming.languages.learning.C++": 1013,
#         "programming.languages.learning.Python": 1014,
#         "programming.languages.learning.C#": 1015,
#         "programming.languages.learning.PHP": 1016,
#         "programming.languages.learning.JavaScript": 1017,
#         "programming.languages.learning.Ruby": 1018,
#         "programming.languages.learning.Kotlin": 1019,
#         "programming.languages.learning.Swift": 1020,
#         "programming.languages.learning.Scala": 1021,
#         "programming.languages.learning.Go": 1022,
#         "programming.languages.learning.R": 1023,
#         "programming.languages.learning.TypeScript": 1024,
#         "programming.languages.learning.Rust": 1025,
#         "programming.languages.learning.Other - Write In": 1026
#     },
#     "ways.to.learn": {
#         "ways.to.learn.I did not learn any new tools / technologies / programming languages in the last 12 months": 1027,
#         "ways.to.learn.Offline educational organizations": 1028,
#         "ways.to.learn.Books": 1029,
#         "ways.to.learn.Personal teacher/consultant": 1030,
#         "ways.to.learn.Online coding schools": 1031,
#         "ways.to.learn.MOOCs (Coursera, edX, Udacity, etc.)": 1032,
#         "ways.to.learn.Blogs/forums": 1033,
#         "ways.to.learn.Documentation & APIs": 1034,
#         "ways.to.learn.Other - Write In": 1035
#     },
#     "tea.or.coffee": {
#         "tea.or.coffee": 1036
#     },
#     "ide.theme": {
#         "ide.theme": 1037
#     },
#     "company.size": {
#         "company.size": 1038
#     },
#     "it.company": {
#         "it.company": 1039
#     },
#     "company.it.industry": {
#         "company.it.industry.Telecom": 1040,
#         "company.it.industry.Game development (including mobile games)": 1041,
#         "company.it.industry.Mobile development": 1042,
#         "company.it.industry.IoT / embedded": 1043,
#         "company.it.industry.IT services": 1044,
#         "company.it.industry.Cloud computing / platform": 1045,
#         "company.it.industry.Big Data / Data analysis": 1046,
#         "company.it.industry.Hardware": 1047,
#         "company.it.industry.Data center services": 1048,
#         "company.it.industry.Software development tools": 1049,
#         "company.it.industry.Internet / Search engines": 1050,
#         "company.it.industry.Semiconductors": 1051,
#         "company.it.industry.E-learning": 1052,
#         "company.it.industry.FinTech": 1053,
#         "company.it.industry.Healthcare IT": 1054,
#         "company.it.industry.Cybersecurity": 1055,
#         "company.it.industry.BPO services": 1056,
#         "company.it.industry.Other Software (all other types of software)": 1057,
#         "company.it.industry.Other - Write In": 1058
#     },
#     "company.industry": {
#         "company.industry.Government and defense": 1059,
#         "company.industry.Administration / Management / Business Development": 1060,
#         "company.industry.Banking / Real Estate / Mortgage Financing / Accounting / Finance / Insurance": 1061,
#         "company.industry.Business / Strategic Management": 1062,
#         "company.industry.Construction / Architecture": 1063,
#         "company.industry.Customer Support": 1064,
#         "company.industry.Design": 1065,
#         "company.industry.Education / Training": 1066,
#         "company.industry.Human Resources": 1067,
#         "company.industry.Law": 1068,
#         "company.industry.Logistics/ Transportation": 1069,
#         "company.industry.Machinery": 1070,
#         "company.industry.Aerospace": 1071,
#         "company.industry.Automotive and boating": 1072,
#         "company.industry.Manufacturing": 1073,
#         "company.industry.Marketing": 1074,
#         "company.industry.Medicine / Health": 1075,
#         "company.industry.Non-profit": 1076,
#         "company.industry.Entertainment / Mass media and information / Publishing": 1077,
#         "company.industry.Restaurants / Hospitality / Tourism": 1078,
#         "company.industry.Sales / Distribution / Retail": 1079,
#         "company.industry.Food / Agriculture": 1080,
#         "company.industry.Science": 1081,
#         "company.industry.Security": 1082,
#         "company.industry.Service / Maintenance": 1083,
#         "company.industry.Energy": 1084,
#         "company.industry.Other - Write In": 1085
#     },
#     "company.development": {
#         "company.development.Product development": 1086,
#         "company.development.Outsourcing": 1087,
#         "company.development.Custom-tailored software / web-sites / applications": 1088,
#         "company.development.In-house development": 1089,
#         "company.development.Internal deployment and maintenance of third-party tools": 1090,
#         "company.development.Customer services development (web-sites, mobile apps, etc.)": 1091,
#         "company.development.Open source projects": 1092,
#         "company.development.Other - Write In": 1093
#     },
#     "it.experience": {
#         "it.experience": 1094
#     },
#     "team.size": {
#         "team.size": 1095
#     },
#     "agile.framework": {
#         "agile.framework": 1096
#     },
#     "pair.programming": {
#         "pair.programming": 1097
#     },
#     "do.advocate": {
#         "do.advocate": 1098
#     },
#     "team.distributed": {
#         "team.distributed": 1099
#     },
#     "age": {
#         "age": 1100
#     },
#     "country": {
#         "country": 1101
#     }
# }