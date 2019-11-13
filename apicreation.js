const express = require('express');
const app =express();
app.get('/getPageData',function(res,req){
    res.header("access-control-allow-origin","*");
    res.json(
        [{
            name:"person1",
            age:22
        },
        {
            name:"person2",
            age:23
        },
        {
            name="person3",
            age:24
        }
    ]);
    
})
app.listen(3000);