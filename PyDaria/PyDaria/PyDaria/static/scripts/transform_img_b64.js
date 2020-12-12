function readFile() {
    if (this.files && this.files[0]) {
      
      var FR = new FileReader();
      
      FR.addEventListener("load", function(e) {
        document.getElementById("previewImg").src = e.target.result;
        document.getElementById("auxInput").value = e.target.result;
        console.log(e.target.result);
      }); 
      
      FR.readAsDataURL( this.files[0] );
    }
}
  
document.getElementById("customFile").addEventListener("change", readFile);