import {createContext} from 'react';


export default createContext({
    isAuth: false,
    login: () => {},
    registration: () => {},
});