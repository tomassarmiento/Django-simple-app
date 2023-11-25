import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {UsersPage} from './pages/UsersPage'
import {Navigation} from './components/Navigation'

function App(){
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/users" element={<UsersPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App