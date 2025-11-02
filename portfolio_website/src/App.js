import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import styled from 'styled-components';
import About from './components/About';
import ContactForm from './components/ContactForm';
import ProjectsList from './components/ProjectsList';

const Nav = styled.nav`
  display: flex;
  background: #282c34;
  padding: 1rem;
  justify-content: center;
  a {
    color: white;
    margin: 0 1rem;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
`;

function App() {
  return (
    <Router>
      <Nav>
        <Link to="/">About</Link>
        <Link to="/projects">Projects</Link>
        <Link to="/contact">Contact</Link>
      </Nav>
      <Routes>
        <Route path="/" element={<About />} />
        <Route path="/projects" element={<ProjectsList />} />
        <Route path="/contact" element={<ContactForm />} />
      </Routes>
    </Router>
  );
}

export default App;
