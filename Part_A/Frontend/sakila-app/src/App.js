import React, { useEffect, useRef, useState } from "react";

//Set Films as constant

//Assign the attributes of Films

const Films = (props) => {
  //Enable the value of Films to be stated and changed

  const [film, setFilms] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/get_films_ordered_by_release_year")
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
        setFilms(json);
      });
  }, []);

  //Return query results
  return (
    <>
      <h1>{props.children}</h1>
      <ul>
        {film.map((film_item) => (
          <li>{film_item}</li>
        ))}
      </ul>
    </>
  );
};

export default Films;
