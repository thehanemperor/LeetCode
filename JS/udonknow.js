sortNamesByLength([
    "Sally",
    "Suzy",
    "Frank",
    "John",
    "Jennifer",
    "Scott"
]);

function sortNamesByLength(names){
    var buckets = [];
    for (let name of names){
        if (buckets[name.length]==null){
            buckets[name.length]=[]
        }
        buckets[name.length].push(name)
    }

    {
        let sortedName = []
        for (let buck of buckets){
            if (buck){
                
                sortedName =[
                    ...sortedName,
                    ...buck
                ]
            }
            
        }
        console.log(sortedName)
    
    }
    
}