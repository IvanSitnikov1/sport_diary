import {instance} from '../api/axios.api';

export const AuthService = {
    async registration(userData) {
        await instance.post('users/', userData);
    },
    async login(userData) {
        const response = await instance.post('auth/token/', userData);
        localStorage.setItem("access", JSON.stringify(response.data.access));
        localStorage.setItem("refresh", JSON.stringify(response.data.refresh));
        localStorage.setItem("isAuth", JSON.stringify(true));
    },
}
