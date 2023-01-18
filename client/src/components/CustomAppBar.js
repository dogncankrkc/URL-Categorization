import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

const CustomAppBar = () => {
  return (
    <Box sx={{ flexGrow: 1 , display:'flex', justifyContent:'start'}}>
      <AppBar position="static">
        <Toolbar sx={{bgcolor:'rgba(1,1,1,.85)'}}>
          <Typography variant="h5" component="div">
            WebCat
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default CustomAppBar;
