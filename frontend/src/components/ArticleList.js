import React from 'react'






function ArticleList(props) {

    const editBtn = (article) => {// receive editBtn from App.js
        props.editBtn(article) //receive editBtn and pass article. editBtn(article)
    }



    return (//props.articles && mean if article in props execute it just to avoid server error in case we dont have articles 

        <div>
        {props.articles && props.articles.map(article => {// map to iterate the articles
        return (// title and description are coming from django database
            <div key={article.id}>
                <h2>{article.title}</h2> 
                <p>{article.description}</p>
                

                <div className="row">
                    <div className="col-md-1">
                        <button className="btn btn-primary" onClick = {() => editBtn(article)}>update</button>
                    </div>

                    <div className="col-md-1">
                        <button className="btn btn-danger">Delete</button>
                    </div>

                </div>

                <hr className = " hrline" />
            </div>
        
        )  

        })}
        </div>
    )
}

export default ArticleList
