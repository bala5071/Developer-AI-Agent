import React from 'react';
import styled from 'styled-components';

const AboutWrapper = styled.section`
  max-width: 750px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: Arial, sans-serif;
`;

const Title = styled.h1`
  text-align: center;
  color: #282c34;
`;

const Paragraph = styled.p`
  font-size: 1.125rem;
  line-height: 1.6;
  margin-bottom: 1rem;
`;

/**
 * About component displays personal profile information.
 * @returns {JSX.Element} React component for About section
 */
function About() {
  return (
    <AboutWrapper>
      <Title>About Me</Title>
      <Paragraph>
        Hello! I'm a passionate web developer with expertise in React and modern JavaScript. I enjoy building responsive and accessible web applications that provide excellent user experiences.
      </Paragraph>
      <Paragraph>
        This portfolio showcases some of my personal projects and skills. Feel free to explore and contact me for collaboration opportunities.
      </Paragraph>
    </AboutWrapper>
  );
}

export default About;
