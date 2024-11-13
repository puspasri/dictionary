student_data={
    "id1":{
        "name": "srishti",
        "grade" : 8
    },
    "id2":{
    "name": "shayan",
    "grade": 7
    },
    "id3":{
        "name": "srishti",
        "grade" : 8
    },
    "id4":{
    "name": "shayan",
    "grade": 7
    },

}

result={
    
}
for key,value in student_data.items():
    if  value  not in  result.values():
       result[key]=value

print(result)

