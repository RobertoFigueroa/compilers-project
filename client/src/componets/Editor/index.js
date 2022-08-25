import React, { useRef,useState } from 'react';


import Editor from "@monaco-editor/react";
import axios from 'axios';

import styles from './styles.module.css';

URL = "http://127.0.0.1:5000"

export const MyEditor = () => {

    const inputRef = useRef(null);
    const [errors, changeErrors] = useState([]);
    const [lines, changeLines] = useState([]);
    const [text, changeText] = useState("");
    const [table, changeTable] = useState([]);

    const handleCompile = () => {
        axios.post(`${URL}/compile`,
        {
            code : text
        })
            .then(response => {
                changeErrors(response.data.errors);
                changeLines(response.data.lines);
                changeTable(response.data.table);
            })
            .catch(error => {
                console.log("Error while compiling", error)
            })
    }

    const handleClick = () => {
        inputRef.current.click();
    };

    const handleFileChange = event => {
        const fileObj = event.target.files && event.target.files[0]
        if (!fileObj) {
            return;
        }

        fileObj.text().then(value => changeText(value));

        // console.log("fileObj is ", fileObj.text());

        event.target.value = null;

    }




    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <h1>YAPL Compiler</h1>
                <input
                    style={{ display: 'none' }}
                    ref={inputRef}
                    type="file"
                    onChange={handleFileChange}
                />
                <div className={styles.buttons}>
                    <button className={styles.btnOpen} onClick={handleClick}>Open file</button>
                    <button className={styles.btnCom} onClick={handleCompile}>Compile</button>
                </div>
            </div>
            <div className={styles.displayContainer}>
                <div className={styles.editor}>
                    <h2>Code</h2>
                    <div className={styles.editordiv}>
                        <Editor
                            height="80vh"
                            defaultLanguage="cool"
                            defaultValue='--happy coding!'
                            theme='vs-dark'
                            value={text}
                            onChange={(v, e) => changeText(v)}
                            />
                    </div>
                </div>
                <div className={styles.errors}>
                    <h2>Console</h2>
                    <div className={styles.errorArea}>
                        {
                            errors.map(e => (
                                <p>{"> "}{e}</p>
                            ))
                        }
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MyEditor;