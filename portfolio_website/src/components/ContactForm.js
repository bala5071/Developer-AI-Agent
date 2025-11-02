import React, { useState } from 'react';
import styled from 'styled-components';

const ContactWrapper = styled.section`
  max-width: 500px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: Arial, sans-serif;
`;

const Title = styled.h1`
  text-align: center;
  color: #282c34;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
`;

const Label = styled.label`
  margin-top: 1rem;
  font-weight: bold;
`;

const Input = styled.input`
  padding: 0.5rem;
  font-size: 1rem;
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

const TextArea = styled.textarea`
  padding: 0.5rem;
  font-size: 1rem;
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  min-height: 100px;
`;

const Button = styled.button`
  margin-top: 1.5rem;
  padding: 0.75rem;
  font-size: 1rem;
  background-color: #007acc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  &:hover {
    background-color: #005fa3;
  }
`;

const ErrorMessage = styled.p`
  color: red;
  margin-top: 0.5rem;
`;

const SuccessMessage = styled.p`
  color: green;
  margin-top: 0.5rem;
  font-weight: bold;
`;

/**
 * Validates email format.
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  const re = /^(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\\.,;:\s@\"]+\.)+[^<>()[\]\\.,;:\s@\"]{2,})$/i;
  return re.test(String(email).toLowerCase());
}

/**
 * ContactForm component provides a form to submit inquiries.
 * @returns {JSX.Element} Contact form component
 */
function ContactForm() {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' });
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  /**
   * Handles input changes
   * @param {React.ChangeEvent<HTMLInputElement|HTMLTextAreaElement>} e
   */
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setErrors({ ...errors, [e.target.name]: '' });
  };

  /**
   * Validates form data
   * @returns {boolean}
   */
  const validate = () => {
    const newErrors = {};
    if (!formData.name.trim()) newErrors.name = 'Name is required';
    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!validateEmail(formData.email)) {
      newErrors.email = 'Invalid email address';
    }
    if (!formData.message.trim()) newErrors.message = 'Message is required';

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0;
  };

  /**
   * Handles form submission with error handling
   * @param {React.FormEvent<HTMLFormElement>} e
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    try {
      // Sending email logic using server or API endpoint (placeholder)
      // Since nodemailer use is backend, here we just simulate success
      // In real use, call API sending message to backend
      setSubmitted(true);
      setFormData({ name: '', email: '', message: '' });
    } catch (error) {
      setErrors({ form: 'Failed to send message. Please try again later.' });
      console.error('Contact form submission error:', error);
    }
  };

  return (
    <ContactWrapper>
      <Title>Contact Me</Title>
      <Form onSubmit={handleSubmit} noValidate>
        <Label htmlFor="name">Name</Label>
        <Input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          aria-describedby="name-error"
          required
        />
        {errors.name && <ErrorMessage id="name-error">{errors.name}</ErrorMessage>}

        <Label htmlFor="email">Email</Label>
        <Input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          aria-describedby="email-error"
          required
        />
        {errors.email && <ErrorMessage id="email-error">{errors.email}</ErrorMessage>}

        <Label htmlFor="message">Message</Label>
        <TextArea
          id="message"
          name="message"
          value={formData.message}
          onChange={handleChange}
          aria-describedby="message-error"
          required
        />
        {errors.message && <ErrorMessage id="message-error">{errors.message}</ErrorMessage>}

        <Button type="submit">Send</Button>
        {errors.form && <ErrorMessage>{errors.form}</ErrorMessage>}
        {submitted && <SuccessMessage>Message sent successfully!</SuccessMessage>}
      </Form>
    </ContactWrapper>
  );
}

export default ContactForm;
