import axios from 'axios';


export const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
})

instance.interceptors.request.use(
  (config) => {
    const token = JSON.parse(localStorage.getItem('access'));
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

instance.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        const originalRequest = {...error.config};
        originalRequest._isRetry = true;
        if (
          error.response.status === 401 &&
          error.config &&
          !error.config._isRetry &&
          !error.config.url.endsWith('auth/refresh/')
        ) {
            const refresh = JSON.parse(localStorage.getItem('refresh'));
            const resp = await instance.post("auth/refresh/", {"refresh": refresh});
            localStorage.setItem("access", JSON.stringify(resp.data.access));
            return instance.request(originalRequest);
        } else if (
            error.response.status === 401 &&
            error.config.url.endsWith('auth/refresh/')
        ) {
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            localStorage.removeItem('isAuth');
            window.location.href = '/auth';
        }
        else {
            console.log('error: ', error);
        }
    }
);
