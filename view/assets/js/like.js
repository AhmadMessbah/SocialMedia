function likeContent(contentId){
    const xhr=new XMLHttpRequest();
    xhr.open('POST','like/content/'+contentId);
    xhr.setRequestHeader('Content-Type','application/json');


    xhr.send(JSON.stringify({contentId}))

    xhr.onload=function (){
        if(xhr.status===200){
            const likeCountElement=document.getElementById('like-count'+contentId);
            const likeButtonElement=document.getElementById('like=button'+contentId);

            const newLikeCount=parseInt(likeCountElement.textContent)+1;
            likeCountElement.textContent=newLikeCount;

            if (!likeButtonElement.classList.contains('liked')) {
                likeButtonElement.classList.add('liked');
            }
        }else {
            console.error('Error liking content',xhr.statusText);

        }
    };

}