import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import {
    Route,
    RouterProvider,
    createBrowserRouter,
    createRoutesFromElements,
} from "react-router-dom";

import {Header} from './components/Header';
import {PrivateRoute} from './components/PrivateRoute';
import {Auth} from './pages/Auth';
import {AboutPage} from './pages/AboutPage';
import {ContactPage} from './pages/ContactPage';


function App() {
    const router = createBrowserRouter(
      createRoutesFromElements(
        <>
          <Route path="/" element={<Header />}>
            <Route element={<PrivateRoute />}>
                <Route path="about" element={<AboutPage />} />
                <Route path="contacts" element={<ContactPage />} />
            </Route>
          </Route>
          <Route path="auth" element={<Auth />} />
        </>
      )
    );

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
