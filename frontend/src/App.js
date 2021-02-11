import './App.css';
// import Navbar from './components/Navbar'
import {useState, useEffect} from 'react'
import ArticleList from './components/ArticleList';
import Form from './components/Form';




function App() {

  const [articles, setArticles] = useState([])//([]) because there is a list 
  const [editArticle, setEditArticle] = useState(null) // create useState for update article
  // we have now the track of article in editArticle we can now send the data to the Form.js 




  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/articles/', {
      'method': 'GET',
      headers: {
        'Content-Type':'application/json',
        'Authorization':'Token 	83dfcfeb7af28b24fc0ce481832d7e2d15b10001'

      }
    })
    .then(resp => resp.json())// convert the response to json
    .then(resp => setArticles(resp))// set the response to articles
    .catch(error => console.log(error))

  }, [])

  // For automatic update in UI
  const UpdatedInformation = (article) => {
    const new_article = articles.map(myarticle => {
      if (myarticle.id === article.id) {
        return article;
      }
      else {
        return myarticle;
      }
    })
    setArticles(new_article)
  }



  // For update article
  const editBtn = (article) => { //send editBtn to ArticleList
    setEditArticle(article) // set the data to editArticle
  }




  return (
    <div className="App">
      <h1>django react project</h1>
      {/* <Navbar        name= "Paulin Mpoyi is the family name" /> */}

      <ArticleList articles={articles} editBtn = {editBtn}/>
      {editArticle ? <Form  article={editArticle}  UpdatedInformation={ UpdatedInformation}/> : null}
    
    </div>
    
  );
}

export default App;
