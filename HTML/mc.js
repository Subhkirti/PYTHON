setTimeout(function(){
    document.getElementById("main").style.visibility="visible";
    document.getElementById("gif").style.visibility="hidden";
}
,1000)
function btn(){
    var text=["New Arival Cold Coffe with Real Milk","Our new App Happiness in your pocket","Notice Beware from Scams","New Arrival A Legend Returns","Saving Worry Spreading Smiles","Now Order Wholesome Whole Wheat","Anniversary Special Treatements Treat From Us!","Happy Meal Nutrition & Fun all in one!"]
    var t=Math.floor(Math.random()*text.length)
    var pics=["https://mcdindia.com/wp-content/uploads/2021/09/img-2.jpg",
    "https://mcdindia.com/wp-content/uploads/2021/04/img-1.jpg","https://mcdindia.com/wp-content/uploads/2021/07/slide-2-new.jpg","https://mcdindia.com/wp-content/uploads/2020/12/home-ff-slide-1-new.jpg","https://mcdindia.com/wp-content/uploads/2020/12/home-ff-slide-5.jpg","https://mcdindia.com/wp-content/uploads/2021/11/img-1.jpg","https://c.tenor.com/Zk1zPNUtl6sAAAAC/mcdonalds-burgers.gif","https://mcdindia.com/wp-content/uploads/2021/11/img-1.jpg"]
    document.getElementById("text").innerHTML=text[t]
    document.getElementById("burger").src=pics[t]
}


