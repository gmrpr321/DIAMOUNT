import React from "react";
import { FiSend } from "react-icons/fi";
import { HiOutlineMenuAlt2 } from "react-icons/hi";
import { FaUserCog, FaPowerOff, FaQuestionCircle } from "react-icons/fa";
import { MdSettings, MdDashboardCustomize } from "react-icons/md";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ScrollToBottom from "react-scroll-to-bottom";
import SvgBackground from "./SvgBackground";
const Index = () => {
  const navigate = useNavigate();
  const [Prompt, setPrompt] = useState("");
  const [promptList, setPromptList] = useState([]);
  const handlePrompt = (e) => {
    setPrompt(e.target.value);
    console.log("hi");
  };
  async function handleSubmit(e) {
    e.preventDefault();
    setPromptList([
      ...promptList,
      { user: "user", message: `${Prompt}` },
      { user: "Ai", message: `${Prompt}` },
    ]);
    console.log("hi");
    setPrompt("");
  }
  return (
    <div className="flex flex-row w-screen h-screen">
      <div className="flex flex-col"></div>
      <div className="flex flex-col w-screen rounded-md shadow-bx mx-auto overflow-auto">
        <ScrollToBottom className="basis-11/12 h-full overflow-y-scroll rounded-md custom-scroll bg-bw-pic1 bg-cover border m-1">
          {promptList.map((message, index) => (
            <Chats key={index} message={message}></Chats>
          ))}
        </ScrollToBottom>
        <form onSubmit={handleSubmit}>
          <div className="flex flex-row xl:h-8 2xl:h-10 rounded-md my-3 mx-5">
            <input
              className="w-full mr-2 xl:my-0.5 rounded-md border p-2 border-black"
              type="text"
              value={Prompt}
              onChange={(e) => {
                setPrompt(e.target.value);
              }}
            ></input>
            <FiSend
              className="my-auto mx-2 xl:w-5 xl:h-5 2xl:w-6 2xl:h-6 cursor-pointer "
              onClick={handleSubmit}
            ></FiSend>
          </div>
        </form>
      </div>
    </div>
  );
};
const Chats = ({ message }) => {
  console.log();
  if (message.message === "" && message.user === "user") return <div></div>;
  if (message.user === "user" && message.message !== "")
    return (
      <div className="flex flex-col my-5 mx-2 h-fit basis-full">
        <div className={`flex h-fit flex-row-reverse`}>
          <div
            className={`xl:text-sm 2xl:text-md bg-black text-white h-fit px-3 py-2 rounded-lg text-center w-5/12`}
          >
            {message.message}
          </div>
        </div>
      </div>
    );
  if (message.user === "Ai" && message.message !== "")
    return (
      <div className="flex flex-col my-5 mx-4 h-5/6 bg-white justify-center shadow-bx1 rounded-lg text-center w-9/12">
        <SvgBackground title={message.message}></SvgBackground>
      </div>
    );
};
export default Index;
