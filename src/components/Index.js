import React from 'react'
import {FiSend} from 'react-icons/fi'
import {HiOutlineMenuAlt2} from 'react-icons/hi'
import {FaUserCog,FaPowerOff,FaQuestionCircle} from 'react-icons/fa'
import {MdSettings,MdDashboardCustomize} from 'react-icons/md'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
// import { useEffect, useRef } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom'
// import {BsSunFill} from 'react-icons/bs'
const Index = () => {
    // const scrollRef = useRef(null);

    // useEffect(() => {
    //   const scrollElement = scrollRef.current;
    //   // Set the scroll position to the bottom of the element
    //   scrollElement.scrollTop = scrollElement.scrollHeight;
    // }, []);
    const navigate=useNavigate(); 
    const [Prompt, setPrompt] = useState("")
    const [prompt, setprompt] = useState([{user:"Ai",message:"this"}])
    const handlePrompt=(e)=>{
        e.preventDefault();
        setPrompt(e.target.value); 
    }
    async function handleSubmit(e){
        e.preventDefault();
        setprompt([...prompt,{ user:"user", message:`${Prompt}`}]);
        setPrompt("");
    }
    return (
    <div className='flex flex-row w-screen h-screen'>
        <div className='flex flex-col w-16 bg-black'>
            <div className='flex flex-col basis-1/2'>
                <HiOutlineMenuAlt2 color='white' size={30} className='mx-auto mt-3 cursor-pointer'></HiOutlineMenuAlt2>
                <FaUserCog color='white' size={25} className='mx-auto mt-10 cursor-pointer'></FaUserCog>
                <MdDashboardCustomize color='white' size={30} className='mx-auto mt-10 cursor-pointer'></MdDashboardCustomize>
                {/* <MdOutlineDashboardCustomize color='white' size={30} className='mx-auto mt-10'></MdOutlineDashboardCustomize> */}
                <FaQuestionCircle color='white' size={25} className='mx-auto mt-10 cursor-pointer'></FaQuestionCircle>
                
            </div>
            <div className='flex flex-col-reverse basis-1/2'>
                <FaPowerOff color='white' size={25} className='mx-auto mb-7 cursor-pointer' onClick={() => {
                navigate("/login", { replace: true });
              }}></FaPowerOff>
                <MdSettings color='white' size={30} className='mx-auto mb-10 cursor-pointer'></MdSettings>
            </div>
        </div>
        <div className='flex flex-col w-full rounded-md shadow-bx m-3 relative'>
            <ScrollToBottom className='basis-11/12 h-full overflow-y-scroll'>
                {prompt.map((message,index)=>(<Chats key={index} message={message}></Chats>))}
            </ScrollToBottom>
            <form onSubmit={handleSubmit}>
            <div className='flex flex-row xl:h-8 2xl:h-10 rounded-md my-auto xl:mx-14 2xl:mx-10 shadow-bx'>
                <FiSend className='my-auto mx-2 xl:w-5 xl:h-5 2xl:w-6 2xl:h-6 cursor-pointer' onClick={handleSubmit}></FiSend>
                <input className='w-full mr-2 xl:my-0.5 2xl:my-1 rounded-md border p-2 border-black' type='text' onChange={handlePrompt}></input>
            </div>
            </form>
        </div>
    </div>
  )
}
const Chats=({message})=>{
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
        <div className='flex flex-col my-5 mx-2 h-5/6 bg-white justify-center border border-black text-center w-2/3'>
            {message.message}
        </div>
    )
}
export default Index
