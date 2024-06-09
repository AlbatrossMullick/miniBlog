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

// function postComment(event){
//     event.preventDefault();
//  console.log(event.target.)
// }

document.querySelectorAll(".comment-form").forEach(form => {

    Object.defineProperty(String.prototype, 'capitalize',{
        value: function(){
            return this.charAt(0).toUpperCase() + this.slice(1);
        },
        enumerable: false,
        configurable: true
    });


    form.addEventListener("submit", function(event){
        event.preventDefault();
        const formData = new FormData(form);
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
        const blogId = form.getAttribute('data-blog-id')
        const comment_section = document.querySelector(`.comment-section[data-comments-blog-id="${blogId}"]`)
        console.log(comment_section)
        const comment_count_update = document.querySelector(`.comment-count[data-comments-blog-id="${blogId}"]`)
        // console.log(comment_section, blogId)
        const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        
        

        // fetching the new comment from the url -> json
        fetch(`/blogs/${blogId}/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken
            },
            body: formData
        }).then(response => response.json()).then(data =>{
            // console.log(data.status)
            if(data.status === "success"){
                // console.log(data.json())
                const date = new Date(data.comment.comment_date)
                date_str = `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}, ${date.toLocaleTimeString('en-US', {hour:'2-digit', minute:'2-digit', hour12:true}).replace("AM","a.m.").replace("PM","p.m.")}`
                new_comment = `<div class="comment text-start" data-comment-id="${data.comment.id}">
                <a href="" class=" btn link-underline link-underline-opacity-0">
                  <blockquote class="blockquote text-start p-2 text-light bg-primary bg-gradient bg-opacity-75 my-1 rounded-4 w-auto">
                    <p>${data.comment.comment}</p>
                    <footer class="blockquote-footer text-start text-light fs-6 opacity-75">${data.comment.comment_by.capitalize()} <cite title="Source Title">(${ date_str })</cite></footer>
                </blockquote>
                </a>
                </div>`;

                if (comment_section.firstElementChild.hasAttribute('class')){
                    comment_list = comment_section.getElementsByClassName('comment');
                    comment_list[comment_list.length - 1].insertAdjacentHTML("afterend", new_comment);        
                } else {
                    comment_section.innerHTML = new_comment;
                }
                comment_count_update.innerText = parseInt(comment_count_update.innerText) + 1;
                console.log(comment_section)
                form.reset();
            } else {
                console.error('Failed to add comment', data.errors || data.error)
            }
        }).catch(error => console.error('Error:', error));


    })

})
