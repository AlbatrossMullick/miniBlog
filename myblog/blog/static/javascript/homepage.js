function readBlog(btn, more, less){
    console.log("hekk")
    read_more = document.getElementById(more.toString())
    read_less = document.getElementById(less.toString())
    
    if (read_more.style.display === 'none'){
        read_less.style.display = 'none'
        read_more.style.display = 'block'
        btn.value = "Read less"
    } else{
        read_less.style.display = 'block'
        read_more.style.display = 'none'
        btn.value = "Read full blog"   
    }

}
