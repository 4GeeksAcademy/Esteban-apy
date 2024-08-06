import React, { useContext } from "react";
import { Context } from "../store/appContext.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	const handleImgError = (event) => {
		// console.log(event.target.src);
		event.target.src = 'https://starwars-visualguide.com/assets/img/placeholder.jpg'

	}

	return (
		<div className="text-center mt-5">
			{/* <Alert/> */}
			{/* <User /> */}
			{/* <Jumbotron/> */}
				
 			<h1>Hello Rigo!!</h1>
			<p>
				<img src={'https://starwars-visualguide.com/assets/img/planets/1.jpg'} 
						onError={handleImgError}/>
			</p>
			<div className="alert alert-info">
				{store.message || "Loading message from the backend (make sure your python backend is running)..."}
			</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://start.4geeksacademy.com/starters/react-flask">
					Read documentation
				</a>
			</p>
			
		</div>
	);
};