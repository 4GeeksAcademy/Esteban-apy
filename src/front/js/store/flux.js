const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [{title: "FIRST", background: "white", initial: "white"},
				     {title: "SECOND", background: "white", initial: "white"}],
			cohorte: 'Spain 72',
			user: 'spain-72',
			host: 'https://playground.4geeks.com/contact',
			alert: {visible: false, back: 'danger', text: 'Mensaje del back'},
			contacts: [],
			currentContact: null,
			currentUser: null,
			isLoged: false
		},
		actions: {
			exampleFunction: () => {getActions().changeColor(0, "green");},
			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => { 
				const store = getStore();  // get the store
				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
			getUsers: async () => {
				const url = 'https://jsonplaceholder.typicode.com/users';
				// const url = `${getStore().host}/agendas/${getStore().user}/contacts`;
				const options = {
					method: 'GET'
				};
				const response = await fetch(url, options);
				if (!response.ok) {
					// Tratar el error
					console.log('error: ', response.status, response.statusText);
					return;
				}
				const data = await response.json();
				console.log(data);  // imprimo en consola el json (el body de response) que me devuelve el fetch()
				// setStore({ contacts: data.contacts});
				setStore({ contacts: data});
				localStorage.setItem('contacts', JSON.stringify(data));
				localStorage.setItem('usuario', getStore().user)
				// La lógica de la app
			},
			getPosts: () => {},
			setAlert: (newAlert) => {setStore({ alert: newAlert})},
			setCurrentContact: (contact) => {setStore({ currentContact: contact })},
			setCurrentUser: (user) => {setStore({ currentUser: user })},
			setIsLoged: (isLogin) => {setStore({ isLoged: isLogin })}
		}
	};
};

export default getState;