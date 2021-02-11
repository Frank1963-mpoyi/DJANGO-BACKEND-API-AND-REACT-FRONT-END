import React, {useState} from 'react'
import APIService from './APIService';



function Form(props) {

    // here we grab our data in title and description
    const [title, setTitle] = useState(props.article.title)
    const [description, setDescriprtion] = useState(props.article.description)



    const UpdateArticle = () => {
        APIService.UpdateArticle(props.article.id, {title, description})
        .then(resp => props.UpdatedInformation(resp))//UpdatedInformation for automatic update in UI

    }


    return (
        <div>
            {props.article ? (

                <div className= "mb-3">
                    <label htmlFor="title" className = "form-label">Title</label>
                    <input type="text" className="form-control" id="title" placeholder= "Please Enter the Title"
                    value= {title} onChange = {e => setTitle(e.target.value)}
                    />
                
                    <label htmlFor="description" className = "form-label">Description</label>
                    <textarea className="form-control" id="description" rows="5"
                    value= {description} onChange = {e => setDescriprtion(e.target.value)}
                    ></textarea>
                    <button onClick = {UpdateArticle}  className="btn btn-success mt-3"> Update Article</button>
                </div>





            ) : null}
        </div>
    )
}


//onChange = {e => setTitle(e.target.value)} want to capture the value of the input text or text you are typing , you are now able to write and delete text inside the input
export default Form
