import React from 'react'
import {FiSend} from 'react-icons/fi'
import {HiOutlineMenuAlt2} from 'react-icons/hi'
import {FaUserCog,FaPowerOff,FaQuestionCircle} from 'react-icons/fa'
import {MdSettings,MdDashboardCustomize} from 'react-icons/md'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import ScrollToBottom from 'react-scroll-to-bottom'
import SvgBackground from './SvgBackground'
const Index = () => {
    const navigate=useNavigate();
    const [Prompt, setPrompt] = useState("")
    const [prompt, setprompt] = useState([])
    const handlePrompt=(e)=>{
        setPrompt(e.target.value);
        console.log("hi") 
    }
    async function handleSubmit(e){
        e.preventDefault();
        setprompt([...prompt,{ user:"user", message:`${Prompt}`},{ user:"Ai", message:`${Prompt}`}]);
        console.log("hi")
        setPrompt("");
    }
    return (
    <div className='flex flex-row w-screen h-screen'>
        <div className='flex flex-col w-16 bg-black'>
            <div className='flex flex-col basis-1/2 px-3'>
                <HiOutlineMenuAlt2 color='white' size={30} className='mx-auto mt-3 cursor-pointer'></HiOutlineMenuAlt2>
                <FaUserCog color='white' size={25} className='mx-auto mt-10 cursor-pointer'></FaUserCog>
                <MdDashboardCustomize color='white' size={30} className='mx-auto mt-10 cursor-pointer'></MdDashboardCustomize>
                <FaQuestionCircle color='white' size={25} className='mx-auto mt-10 cursor-pointer'></FaQuestionCircle>
                
            </div>
            <div className='flex flex-col-reverse basis-1/2 px-3'>
                <FaPowerOff color='white' size={25} className='mx-auto mb-7 cursor-pointer' onClick={() => {
                navigate("/login", { replace: true });
              }}></FaPowerOff>
                <MdSettings color='white' size={30} className='mx-auto mb-10 cursor-pointer'></MdSettings>
            </div>
        </div>
        <div className='flex flex-col w-11/12 rounded-md shadow-bx mx-auto my-3 overflow-auto'>
            <ScrollToBottom className='basis-11/12 h-full overflow-y-scroll custom-scroll'>
                {
                    prompt.map((message,index)=>(<Chats key={index} message={message}></Chats>))
                }
            </ScrollToBottom>
            <form onSubmit={handleSubmit}>
            <div className='flex flex-row xl:h-8 2xl:h-10 rounded-md my-auto xl:mx-14 2xl:mx-10 shadow-bx'>
                <FiSend className='my-auto mx-2 xl:w-5 xl:h-5 2xl:w-6 2xl:h-6 cursor-pointer' onClick={handleSubmit}></FiSend>
                <input className='w-full mr-2 xl:my-0.5 2xl:my-1 rounded-md border p-2 border-black' type='text' value={Prompt} onChange={(e)=>{setPrompt(e.target.value)}}></input>
            </div>
            </form>
        </div>
    </div>
  )
}
const Chats=({message})=>{
    console.log()
    if(message.message==="" && message.user==="user")
    return(<div></div>)
    if(message.user==="user" && message.message!=="")
    return(
    <div className='flex flex-col my-5 mx-2 h-fit basis-full'>
        <div className={`flex h-fit flex-row-reverse`}>
            <div className={`bg-black text-white h-fit px-3 py-2 rounded-lg text-center ${message.user==="user" && "w-5/12"}`}>
                {message.message}
            </div>
        </div> 
    </div>
    )
    if(message.user==="Ai" && message.message!=="")
    return(
        <div className='flex flex-col my-5 mx-4 h-5/6 bg-white justify-center shadow-bx rounded-lg text-center w-9/12'>
            <SvgBackground title={message.message}></SvgBackground>
        </div>
    )
}
export default Index
