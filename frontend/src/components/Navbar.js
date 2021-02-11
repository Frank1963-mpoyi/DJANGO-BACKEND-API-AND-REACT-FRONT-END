import React from 'react'

function Navbar(props) {
    return (
        <div>
            <h1> Mpoyi wa Tshibuyi</h1>
            <p>lorem doest not want to work in react app <br/>
                My family name is : {props.name}
            </p>
        </div>
    )
}

export default Navbar
