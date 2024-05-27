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
    console.log(form)
    form.addEventListener("submit", function(event){
        event.preventDefault();
        const formData = new FormData(form);
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;
        const blogId = form.getAttribute('data-blog-id')
        const comment_section = document.querySelector(`.comment-section[data-comments-blog-id="${blogId}"]`).lastElementChild
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
                const date = new Date(data.comment_date)
                date_str = `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}, ${date.toLocaleTimeString('en-US')}`
                new_comment = `<div class="comment text-start" data-comment-id="${data.comment.id}">
                <a href="" class=" btn link-underline link-underline-opacity-0">
                  <blockquote class="blockquote text-start p-2 text-light bg-primary bg-gradient bg-opacity-75 my-1 rounded-4 w-auto">
                    <p>${data.comment.comment}</p>
                    <footer class="blockquote-footer text-start text-light fs-6 opacity-75">${date_str} <cite title="Source Title">(${ data.comment.comment_date })</cite></footer>
                </blockquote>
                </a>
                </div>`;
                comment_section.insertAdjacentHTML("beforeend", new_comment);
                console.log(comment_section)
                form.reset();
            } else {
                console.error('Failed to add comment', data.errors || data.error)
            }
        }).catch(error => console.error('Error:', error));


    })

})


// document.getElementById('comment-form').addEventListener('submit', function(event){
//     event.preventDefault();

//     const comment = document.getElementById('id_comment').value;
//     const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

//     fetch("{% url 'add_comment' blog.id %}", {
//         method:"POST",
//         headers:{
//             "content-Type":"application/json",
//             "X-CSRFToken": csrfToken
//         },
//         body: JSON.stringify({
//             comment:comment
//         })
//     }).then(response => response.json()).then( data =>{
//         if (data.success === 'success'){
//             html = "<div class='text-start'>
//             <a href='' class='btn link-underline link-underline-opacity-0'>
//               <blockquote class='blockquote text-start p-2 text-light bg-primary bg-gradient bg-opacity-75 my-1 rounded-4 w-auto'>
//                 <p>" +data.comment+ "</p>
//                 <footer class='blockquote-footer text-start text-light fs-6 opacity-75'>" +data.user+ "<cite title='Source Title'>("+ data.comment.comment_date +")</cite></footer>
//             </blockquote>
//             </a>
//             </div>"
//             document.getElementById('comment-section').innerHTML +=html;
//         }
//     })

// })