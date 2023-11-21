function edit(id){

}

async function remove(id){
    await fetch("/profile?id="+id, {
        method:"DELETE"
    });

    document.location.replace("/profile");
}