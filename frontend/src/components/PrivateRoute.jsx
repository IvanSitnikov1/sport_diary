import {useContext} from 'react';
import { Navigate, Outlet } from 'react-router-dom';

import AuthContext from '../contexts/AuthContext';


export const PrivateRoute = () => {
    const {isAuth} = useContext(AuthContext);

    if (isAuth) {
        return <Outlet/>;
    } else {
        return <Navigate to="/auth" />;
    }
};
