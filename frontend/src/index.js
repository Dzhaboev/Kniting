import React from 'react';
import ReactDOM from 'react-dom';
import '../public/assets/scss/main.scss';

function Hero() {
    return(
        <div>
            <h1>REACT</h1>
        </div>
    );
}

ReactDOM.render(<Hero />, document.getElementById('app'));