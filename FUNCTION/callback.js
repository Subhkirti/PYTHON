// 1)
// function show(){
//     console.log("Hello World!")
// }
// function hide(callback){
//     callback();
//     console.log("after I am")
// }
// hide(show)

// // 2)
// function show(a){
//     console.log("I am from",a)
// }
// function hide(callback){
//     callback
// }
// hide(show("Punjab"))

// // 3)
// function hide(callback){
//     callback()
//     console.log("I am after")
// }
// hide(function show(){
//     console.log("hello world!")
// })

// // 4)
// function hide(callback){
//   callback()
// }
// hide(function(){
//     console.log("hello world!")
// })

 // // 5)
// var hide=(callback)=>callback();
// console.log("Before I am");
// hide(()=>console.log("Hello world!"))

// // // 6)
// function hide(callback){
//       callback()
//       console.log("After I am")
//     }
// hide(()=>console.log("Hello world"))

