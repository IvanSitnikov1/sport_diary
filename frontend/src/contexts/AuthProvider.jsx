import {useState} from 'react';

import AuthContext from './AuthContext';
import {AuthService} from '../services/auth.service';


const AuthProvider = ({children}) => {
    const [isAuth, setIsAuth] = useState(JSON.parse(localStorage.getItem('isAuth')) || false);

    const login = async (userData) => {
        try {
            await AuthService.login(userData);
            setIsAuth(true);
        } catch (error) {
            console.log("login error", error);
        }
    };

    const registration = async (userData) => {
        try {
            await AuthService.registration(userData);
        } catch (error) {
            console.log("login error", error);
        }
    };

    return (
        <AuthContext.Provider value={{isAuth, login, registration}}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider
