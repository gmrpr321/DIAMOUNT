import React from 'react'
import {FcGoogle} from 'react-icons/fc';
import {BiShow,BiHide} from 'react-icons/bi';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
const Login = () => {
    const [show, setShow] = useState("password")
    const [visible, setVisible] = useState("visible")
    const [invisible,setInvisible] = useState("hidden")
    const navigate=useNavigate();
    const makeVisible=()=>{
      setShow("text");
      setInvisible("visible");
      setVisible("hidden");
    }
    const makeInvisible=()=>{
      setShow("password");
      setInvisible("hidden");
      setVisible("visible");
    }
    return (
      <div className='flex flex-row w-screen h-screen'>
        <div className='bg-black basis-1/2 relative'></div>
        <div className='flex flex-row left-1/4 xl:top-28 2xl:top-32 shadow-bx bg-white h-4/6 w-2/4 absolute'>
          <div className='basis-1/2 flex flex-col'>
            <div className='text-center xl:mt-10 2xl:mt-14 xl:text-2xl 2xl:text-4xl welcome'>Welcome User</div>
            <div className='flex flex-col xl:ml-6 2xl:ml-8 mt-5'>
              <div className='xl:text-sm 2xl:text-md font-semibold xl:mb-1 2xl:mb-2'>User Name:</div>
              <input className='input xl:text-xs 2xl:text-sm w-11/12 h-7' type='text'></input>
            </div>
            <div className='flex flex-col xl:ml-6 2xl:ml-8 xl:mt-6 2xl:mt-8'>
              <div className='xl:text-sm 2xl:text-md font-semibold xl:mb-1 2xl:mb-2'>Password:</div>
              <div className='w-11/12 flex flex-row-reverse'>
                <div className='absolute xl:mt-2 2xl:mt-1'>
                  <BiShow className={`2xl:w-5 2xl:h-5 cursor-pointer ${visible}`} onClick={makeVisible}></BiShow>
                  <BiHide className={`2xl:w-5 2xl:h-5 cursor-pointer ${invisible}`} onClick={makeInvisible}></BiHide>
                </div>
                <input className='input xl:text-xs 2xl:text-sm w-full h-7' type={show}></input>
              </div>
            </div>
            <div className='w-fit h-fit px-4 py-1 rounded-md mx-auto xl:text-sm xl:mt-8 2xl:mt-10 shadow-bx bg-black text-white cursor-pointer' onClick={() => {
                navigate("/index", { replace: true });
              }}>Log In</div>
            <div className='flex flex-row xl:ml-10 2xl:ml-12 xl:mt-4 2xl:mt-6'>
              <hr className='basis-5/12 h-0.5 my-auto' color='black'></hr>
              <div className='xl:mb-1 xl:text-xs 2xl:text-sm font-medium'>or</div>
              <hr className='basis-5/12 h-0.5 my-auto' color='black'></hr>
            </div>
            <div className='xl:mt-4 2xl:mt-6 mx-auto shadow-bx h-8 w-fit rounded-md cursor-pointer flex flex-row'>
              <FcGoogle className='my-auto mx-2 2xl:w-6 2xl:h-6 xl:w-5 xl:h-5'></FcGoogle>
              <div className='xl:text-sm 2xl:text-md font-semibold my-auto mr-2'>Continue with Google</div>
            </div>
            <div className='mt-3 mx-auto flex flex-row'>
                <div className='xl:text-xs 2xl:text-sm'>Don't have an account?</div>
                <div className='xl:text-xs 2xl:text-sm text-blue-700 underline cursor-pointer ml-1' onClick={() => {
                navigate("/signup", { replace: true });
              }}>Create account</div>
            </div>
          </div>
          <div className='basis-1/2'></div>
        </div>
      </div>
    )
  }

export default Login