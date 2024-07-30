let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// ensure search form exists
if(searchForm){
  for(let i=0;i<pageLinks.length;i++){
    pageLinks[i].addEventListener('click',function(e){
      e.preventDefault()

      // get data attribute
      let page = this.dataset.page

      // construct a parameter to add to searchFormHTML
      // note : this is ` this character
      searchForm.innerHTML += `<input value=${page} name="page" hidden>'`

      searchForm.submit()
    })
  }
}
