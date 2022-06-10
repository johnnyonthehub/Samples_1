import React, { useState, useRef, useEffect } from "react";

const PostCountry = (props) => {
  const country_grab = useRef();
  const postCountry = () => {
    const country_name = country_grab.current.value;
    fetch(
      `http://127.0.0.1:8000/insert_new_country_record?country_name=${country_name}`,
      {
        method: "POST",
      }
    );
  };
  return (
    <>
      <form>
        <input ref={country_grab} type="text" />
        <button onClick={postCountry}>Enter Country Name</button>
      </form>
    </>
  );
};

export default PostCountry;

// function MakePost() {
//   const [name] = useState([]);
//   const MakePost = useRef();

//   function add_new_country(name) {
//   fetch("http://127.0.0.1:8000/insert New Country Record?country_name'", {
//     method: "POST",
//     headers: {
//       "Content-type": "application/json",
//     },
//     body: JSON.stringify(MakePost),
//   });
// }
