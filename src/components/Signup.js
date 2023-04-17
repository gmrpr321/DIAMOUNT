import React from 'react'
import {FcGoogle} from 'react-icons/fc';
import {BiShow,BiHide} from 'react-icons/bi';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
const Signup = () => {
    const navigate=useNavigate();
    const [show, setShow] = useState("password")
    const [visible, setVisible] = useState("visible")
    const [invisible,setInvisible] = useState("hidden")
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
        <div className='flex flex-row left-1/4 top-28 shadow-bx bg-white h-4/6 w-2/4 absolute'>
          <div className='basis-1/2 flex flex-col'>
            <div className='text-center mt-7 create'>Create Account</div>
            <div className='flex flex-col ml-10 mt-5'>
              <div className='text- font-semibold mb-1'>User Name:</div>
              <input className='input text-sm w-11/12 h-7' type='text'></input>
            </div>
            <div className='flex flex-col ml-10 mt-5'>
                <div className='text-md font-semibold mb-1'>Email:</div>
                <input className='input text-sm w-11/12 h-7' type="email"></input>
            </div>
            <div className='flex flex-col ml-10 mt-5'>
              <div className='text-md font-semibold mb-1'>Password:</div>
              <div className='w-11/12 flex flex-row-reverse'>
                <div className='absolute mt-1'>
                  <BiShow className={`cursor-pointer ${visible}`} size={19} onClick={makeVisible}></BiShow>
                  <BiHide className={`cursor-pointer ${invisible}`} size={19} onClick={makeInvisible}></BiHide>
                </div>
                <input className='input text-sm w-full h-7' type={show}></input>
              </div>
            </div>
            <div className='w-fit h-fit px-4 py-1 rounded-md mx-auto mt-7 shadow-bx bg-black text-white cursor-pointer'>Sign up</div>
            <div className='flex flex-row ml-12 mt-4'>
              <hr className='basis-5/12 h-0.5 my-auto' color='black'></hr>
              <div className='text-sm font-medium'>or</div>
              <hr className='basis-5/12 h-0.5 my-auto' color='black'></hr>
            </div>
            <div className='mt-6 mx-auto shadow-bx h-8 w-fit rounded-md cursor-pointer flex flex-row'>
              <FcGoogle size={25} className='my-auto mx-2'></FcGoogle>
              <div className='text-md font-semibold my-auto mr-2'>Sign up with Google</div>
            </div>
            <div className='mt-2 mx-auto flex flex-row'>
                <div className='text-sm'>Already an user?</div>
                <div className='text-sm text-blue-700 underline cursor-pointer ml-1' onClick={() => {
                navigate("/login", { replace: true });
              }}>Login</div>
            </div>
          </div>
          <div className='basis-1/2'></div>
        </div>
      </div>
    )
  }

export default Signup