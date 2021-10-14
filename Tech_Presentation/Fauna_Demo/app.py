# imports
import re
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

# Establish secret key
client = FaunaClient(secret='fnAEVbodhLACROAhawUV2aEWVGukrPmG4mpx23jD')
print(' ')

# Creating a new row in a table
# client.query(
#         q.create(
#             q.collection('Students'),
#             {"data": {"Student": "Bob", "Year": "Freshman", "GPA": "2.3"}}
#             ))

# Retrieving data from an index
allStudents = client.query(
                q.paginate(
                    q.match(
                        q.index('allStudents')
                        )))
studentList = [allStudents['data']]

# print(studentList)

output = re.findall('\d+', str(studentList))

# Formatting Data output
for i in range(0, len(output), 1):
    studentInfo = client.query(q.get(q.ref(q.collection('Students'), output[i])))
    studentInfoList = [studentInfo['data']]

    print("Student:", studentInfoList[0].get("Student"))
    print("Year:", studentInfoList[0].get("Year"))
    print("GPA:", studentInfoList[0].get("GPA"))
    print("______________________")
