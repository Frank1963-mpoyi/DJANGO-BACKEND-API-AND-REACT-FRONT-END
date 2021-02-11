//import React from 'react'


export default class APIService {
    static UpdateArticle(article_id, body) {
        // want to update according to the id that why we put article_id after fetching our api
        return fetch(`http://127.0.0.1:8000/api/articles/${article_id}/`, {
            'method': 'PUT', //bcz we update
            headers: {
                'Content-Type':'application/json',
                'Authorization':'Token 	83dfcfeb7af28b24fc0ce481832d7e2d15b10001'
    
            },
            body:JSON.stringify(body)
    
        }).then(resp => resp.json()) // convert the data to json 
        
    }
}

//export default APIService;