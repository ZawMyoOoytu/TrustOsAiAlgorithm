import React from "react";


export default function ExecutionResult({ result }) {

    if (!result) {
        return null;
    }


    return (
        <div className="execution-result">

            <h2>
                {result.title || "Execution Result"}
            </h2>


            <p>
                {result.description}
            </p>


            {/* FILE LIST */}
            {result.files && (
                <div>

                    <h3>
                        Generated Files
                    </h3>


                    {result.files.map((file,index)=>(
                        <div
                            key={index}
                            className="file-box"
                        >

                            <h4>
                                {file.name}
                            </h4>


                            <pre>
                                {file.content}
                            </pre>

                        </div>
                    ))}

                </div>
            )}



            {/* STEPS */}
            {result.steps && (
                <div>

                    <h3>
                        Steps
                    </h3>


                    <ul>
                    {
                        result.steps.map(
                            (step,index)=>(
                                <li key={index}>
                                    {step}
                                </li>
                            )
                        )
                    }
                    </ul>

                </div>
            )}


        </div>
    );
}