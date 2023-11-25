import {Link} from 'react-router-dom';

export function Navigation() {
  return (
    <div>
        <h1>Users</h1>
        <Link to="/users">Users</Link>
    </div>
  )
}