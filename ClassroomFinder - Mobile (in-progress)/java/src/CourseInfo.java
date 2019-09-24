public class CourseInfo {
        String code;
        String title;
        String day;
        String time;
        String room;
        String instructor;

        public CourseInfo(String codeTemp, String titleTemp, String dayTemp, String timeTemp, String roomTemp, String instructorTemp) {
                code = codeTemp;
                title = titleTemp;
                day = dayTemp;
                time = timeTemp;
                room = roomTemp;
                instructor = instructorTemp;
        }

        public String getCode(){
                return code;
        }
        public void setCode(String newCode) {
                code = newCode;
        }

        public String getTitle(){
                return title;
        }
        public void setTitle(String newTitle){
                title = newTitle;
        }

        public String getDay(){
                return day;
        }
        public void setDay(String newDay){
                day = newDay;
        }

        public String getTime(){
                return time;
        }
        public void setTime(String newTime){
                time = newTime;
        }

        public String getRoom(){
                return room;
        }
        public void setRoom(String newRoom){
                room = newRoom;
        }

        public String getInstructor(){
                return instructor;
        }
        public void setInstructor(String newInstructor){
                instructor = newInstructor;
        }
}
