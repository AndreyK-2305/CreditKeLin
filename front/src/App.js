import './App.css'; 
import 'mdb-react-ui-kit/dist/css/mdb.min.css'; 
import React from 'react';
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput
} from 'mdb-react-ui-kit';

function App() {
  return (
    <MDBContainer className="full-height-container gradient-form">

      <MDBRow>

        <MDBCol col='6' className="mb-5">
          <div className="d-flex flex-column ms-5">

            <div className="text-center">
              <img src="/logo.webp" className="round-img" alt="logo" style={{width: '180px', borderRadius: '50%'}}/>
              <h4 className="mt-1 mb-5 pb-1">Bienvenido a CreditKelin</h4>
            </div>

            <p>Please login to your account</p>

            <MDBInput wrapperClass='mb-4' label='Email address' id='form1' type='email'/>
            <MDBInput wrapperClass='mb-4' label='Password' id='form2' type='password'/>

            <div className="text-center pt-1 mb-5 pb-1">
              <MDBBtn className="mb-4 w-100 gradient-custom-2">Sign in</MDBBtn>
              <a className="text-muted" href="#!">Web unicamente para empleados</a>
            </div>

          </div>
        </MDBCol>

        <MDBCol col='6' className="mb-5">
          <div className="d-flex flex-column justify-content-center gradient-custom-2 h-100 mb-4">

            <div className="text-white px-3 py-4 p-md-5 mx-md-4">
              <h4 className="mb-4">Acerca de este proyecto</h4>
              <p className="small mb-0">CreditKelin es una iniciativa(proyecto para la materia ProgramacionWeb)
                de estudiantes de Ingenieria de Sistemas de la Universidad Fransisco de Paula Santander. <br />   <br />
                Autores:<br /><br />  - Kevin Jaimes    1152245<br />
                          - Evelin Bermudez 1152278
              </p>
            </div>

          </div>
        </MDBCol>

      </MDBRow>

    </MDBContainer>
  );
}

export default App;
