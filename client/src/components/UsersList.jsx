import {getAllUsers} from '../api/users.api'
import {useEffect} from 'react'

export function UsersList(){

    //useEffect
    useEffect(() => {
      async function loadTasks() {
        const res = await getAllUsers()
        console.log(res)
      }

        loadTasks()
    }, [])
    
  return (
    <div>UsersList</div>
  )
}