import { useState } from "react";
import axios from "axios";
import CustomAppBar from "./components/CustomAppBar";
import {
  Button,
  Box,
  TextField,
  MenuItem,
  FormControl,
  Select,
  Typography,
  Alert,
} from "@mui/material";
import "./style/index.css";

function App() {
  const [input, setInput] = useState();
  const [mainCategory, setMainCategory] = useState("");
  const [subCategory, setSubCategory] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isConfirmed, setIsConfirmed] = useState(false);

  const [type, setType] = useState(".com");
  const [domain, setDomain] = useState("");

  const [error, setError] = useState(false);

  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  const handleChangeType = (event) => {
    setType(event.target.value);
  };

  const handleChangeDomain = (e) => {
    setDomain(e.target.value);
  };

  function handleChangeInput(e) {
    setInput(domain + type);
    setIsConfirmed(true);

    const timer = setTimeout(() => {
      setIsConfirmed(false);
    }, 2000);
    return () => clearTimeout(timer);
  }

  const getCat = () => {
    axios
      .get("/cat")
      .then((response) => {
        setMainCategory(response.data[0]);
        setSubCategory(response.data[1]);
      })
      .catch((err) => {
        setError(true);
      })
      .then(async () => {
        setIsSubmitting(false);
        await sleep(2000);
        setError(false);
      });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    const body = {
      input: input,
    };
    axios.post("/cat", body);
    await sleep(2000);
    getCat();
  };

  const submitButtonText = `${!isSubmitting ? "Find Category" : "Loading"}`;
  const disabledSubmitButton = !isSubmitting ? false : true;

  const confirmButtonColor = `${!isConfirmed ? "warning" : "success"}`;
  const confirmButtonText = `${!isConfirmed ? "Confirm Domain" : "Confirmed"}`;

  return (
    <Box className="App">
      <CustomAppBar />
      <Box className="content">
        <Box className="form">
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              lineHeight: "5rem",
            }}
          >
            <form>
              <TextField
                disabled
                placeholder="http://"
                sx={{ maxWidth: "6rem" }}
              ></TextField>
              <TextField
                placeholder="Type Your URL"
                onChange={handleChangeDomain}
                name="url"
                sx={{ minWidth: "35rem" }}
              />
            </form>
            <Box sx={{ minWidth: 120 }}>
              <FormControl fullWidth>
                <Select
                  id="demo-simple-select"
                  value={type}
                  onChange={handleChangeType}
                  defaultChecked=".com"
                >
                  <MenuItem value={".com"}>.com</MenuItem>
                  <MenuItem value={".com.tr"}>.com.tr</MenuItem>
                  <MenuItem value={".org"}>.org</MenuItem>
                  <MenuItem value={".net"}>.net</MenuItem>
                </Select>
              </FormControl>
            </Box>
          </div>
          <Box>
            <Button
              variant="contained"
              color={confirmButtonColor}
              onClick={handleChangeInput}
              sx={{ marginRight: "1rem" }}
            >
              {confirmButtonText}
            </Button>
            <Button
              type="submit"
              variant="contained"
              color="info"
              onClick={handleSubmit}
              disabled={disabledSubmitButton}
            >
              {submitButtonText}
            </Button>
          </Box>
        </Box>

        <Box className="result">
          {mainCategory && (
            <Box
              sx={{
                justifyContent: "center",
                alignItems: "center",
                bgcolor: "transparent",
              }}
            >
              <Typography color="secondary" fontWeight="650" variant="h6">
                <span style={{ color: "rgba(1,1,1,.7)" }}>
                  Main Category &rarr;
                </span>{" "}
                {mainCategory}
              </Typography>
            </Box>
          )}

          {subCategory && (
            <Box
              sx={{
                justifyContent: "center",
                alignItems: "center",
                bgcolor: "transparent",
              }}
            >
              <Typography color="secondary" fontWeight="650" variant="h6">
                <span style={{ color: "rgba(1,1,1,.7)" }}>
                  Sub Category &rarr;
                </span>{" "}
                {subCategory}
              </Typography>
            </Box>
          )}
        </Box>
        {error && (
          <Box
            sx={{
              position: "fixed",
              left: 0,
              bottom: 0,
              width: "100%",
              borderRadius: "0",
            }}
          >
            <Alert variant="filled" severity="error">
              An Error Occurred!
            </Alert>
          </Box>
        )}
      </Box>
    </Box>
  );
}

export default App;
