console.log('Hello jas')

const copybtns =[...document.getElementsByClassName('copy-btn')]
console.log(copybtns)

copybtns.forEach(btn=> btn.addEventListener('click', ()=>{
    console.log('click')
    const imageLink = btn.getAttribute('data-hex')
    console.log(imageLink)
    navigator.clipboard.writeText(imageLink)
    btn.textContent = 'Link Copied ^_^'
    
}))

// $(".bg3").mouseover(function(){
//     $(".btn3").show();
// });
// $(".bg3").mouseleave(function(){
//     $(".btn3").hide();
// });
